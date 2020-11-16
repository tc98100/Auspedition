import urllib

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import viewsets
from django.db.models import Q
from .decorators import *

from .forms import CreateUserForm, ChangeUserInfo, ChangePicBio, EditRecommendation, AddCommentAttraction
from .models import *
from .serializers import *


def edit(request, recommendation):
    specific_recommendation = Recommendation.objects.get(recommendation_id=recommendation)
    if request.method == 'POST':
        edit_form = EditRecommendation(request.POST, request.FILES, instance=specific_recommendation)
        if edit_form.is_valid:
            edit_form.save()
    else:
        edit_form = EditRecommendation(instance=specific_recommendation)
    context = {'recommendation': specific_recommendation, 'edit': edit_form}
    return render(request, "staff_recommendation.html", context)


@login_required(login_url='login_user')
def profile(request):
    return render(request, "profile.html")


@login_required(login_url='login_user')
def profile_change(request):
    if request.method == 'POST':
        change_form = ChangeUserInfo(request.POST, instance=request.user)
        change_pic_bio = ChangePicBio(request.POST, request.FILES, instance=request.user.userinfo)
        if change_form.is_valid and change_pic_bio.is_valid:
            change_form.save()
            change_pic_bio.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        change_form = ChangeUserInfo(instance=request.user)
        change_pic_bio = ChangePicBio(instance=request.user.userinfo)
    return render(request, "profile_change.html", {'change_form': change_form, 'change_pic': change_pic_bio})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password :(')
    return render(request, 'login_user.html')


def logout_user(request):
    logout(request)
    return redirect('home')


@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')

            UserInfo.objects.create(
                user=new_user,
            )

            messages.success(request, 'Sign up successful for ' + username)
            return redirect('login_user')
    return render(request, 'signup.html', {'form': form})


def home(request):
    Destinations = Destination.objects.order_by('likes')[:3]
    Attractions = Attraction.objects.order_by('likes')[:3]
    Recommendations = Recommendation.objects.all()[:3]
    context = {'Destinations': Destinations, 'Attractions': Attractions, 'Recommendations': Recommendations}
    return render(request, 'home.html', context)


def destination_list(request):
    Destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'Destinations': Destinations})


def attraction_list(request):
    Attractions = Attraction.objects.all()
    city_list = []
    for attraction in Attractions:
        if attraction.city.name not in city_list:
            city_list.append(attraction.city.name)
    return render(request, 'attractions.html', {'Attractions': Attractions, 'city_list': city_list})


def detailed_destination(request, destination):
    city = Destination.objects.get(destination_id=destination)
    comments = city.destinationcomment_set.all()
    if request.method == 'POST':
        add_comment = request.POST.get('add_comment')
        DestinationComment.objects.create(
            user=request.user,
            comment_on=city,
            comment_content=add_comment
        )
    context = {'city': city, 'comments': comments}
    return render(request, "destination_detail.html", context)


def detailed_attraction(request, attraction):
    place = Attraction.objects.get(attraction_id=attraction)
    comments = place.attractioncomment_set.all()
    if request.method == 'POST':
        add_comment = request.POST.get('add_comment')
        AttractionComment.objects.create(
            user=request.user,
            comment_on=place,
            comment_content=add_comment
        )
    context = {'place': place, 'comments': comments}
    return render(request, "attraction_detail.html", context)


def delete_comment_attraction(request, comment_id):
    comment = AttractionComment.objects.get(commentId=comment_id)
    comment.delete()
    return render(request, 'test.html', {'comment': comment})


def delete_comment_destination(request, comment_id, destination):
    city = Destination.objects.get(destination_id=destination)
    comment = DestinationComment.objects.get(commentId=comment_id)
    comment.delete()
    context = {'comment': comment, 'city': city}
    return render(request, 'test.html', {'comment': comment})


def detailed_recommendation(request, recommendation):
    specific_recommendation = Recommendation.objects.get(recommendation_id=recommendation)
    return render(request, "recommendation.html", {'recommendation': specific_recommendation})


def search_result(request):
    user_input = ''
    match = True

    if request.method == 'GET':
        user_input = request.GET.get('input')

    condition1 = Q(name__icontains=user_input) | Q(stateCode__icontains=user_input) | Q(state__icontains=user_input)
    condition2 = Q(name__icontains=user_input) | Q(city__name__icontains=user_input) | \
                 Q(city__state__icontains=user_input) | Q(city__stateCode__icontains=user_input)

    result_destination = Destination.objects.filter(condition1)
    result_attraction = Attraction.objects.filter(condition2)
    result_recommendation = Recommendation.objects.filter(title__icontains=user_input)

    if not result_destination and not result_attraction and not result_recommendation:
        match = False
        result_destination = Destination.objects.all()[:3]
        result_attraction = Attraction.objects.all()[:3]

    context = {'cities': result_destination, 'places': result_attraction, 'rec': result_recommendation, 'match': match}
    return render(request, "search_result.html", context)


def filter_state(request):
    state = ''
    match = True
    if request.method == 'GET':
        state = request.GET.get('state')

    if state == 'STATE':
        cities = Destination.objects.all()
    else:
        cities = Destination.objects.filter(stateCode=state)
    return render(request, "search_result.html", {'cities': cities, 'match': match})


def filter_city(request):
    city = ''
    match = True
    if request.method == 'GET':
        city = request.GET.get('city')

    if city == 'CITY':
        places = Attraction.objects.all()
    else:
        places = Attraction.objects.filter(city__name=city)
    return render(request, "search_result.html", {'places': places, 'match': match, 'city': city})

# def count_increment_dest(destination):
#     city = Destination.objects.get(destination_id=destination)
#     city.click_count += 1
#     city.save(update_fields=['click_field'])

class DestinationModelViewSet(viewsets.ModelViewSet):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserInfo.objects.all()


class AttractionModelViewSet(viewsets.ModelViewSet):
    serializer_class = AttractionSerializer
    queryset = Attraction.objects.all()


class DestinationCommentModelViewSet(viewsets.ModelViewSet):
    serializer_class = DestinationCommentSerializer
    queryset = DestinationComment.objects.all()


class AttractionCommentModelViewSet(viewsets.ModelViewSet):
    serializer_class = AttractionCommentSerializer
    queryset = AttractionComment.objects.all()


class RecommendationModelViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
