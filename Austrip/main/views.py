import urllib

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.db.models import Q,F
from .decorators import *
from django_filters.rest_framework import DjangoFilterBackend

from .forms import CreateUserForm, ChangeUserInfo, ChangePicBio, EditRecommendation, AddCommentAttraction
from .models import *
from .serializers import *
from django.http import HttpResponse

def edit(request, recommendation):
    specific_recommendation = Recommendation.objects.get(recommendation_id=recommendation)
    if request.method == 'POST':
        edit_form = EditRecommendation(request.POST, request.FILES, instance=specific_recommendation)
        if edit_form.is_valid:
            edit_form.save()
    else:
        edit_form = EditRecommendation(instance=specific_recommendation)
    return render(request, "staff_recommendation.html", {'recommendation': specific_recommendation, 'edit': edit_form})


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
            response = redirect('home')
            response.set_cookie('username', request.POST.get('username'), 60)
            return response
        else:
            messages.info(request, 'Invalid username or password :(')
    return render(request, 'login_user.html')


def logout_user(request):
    response = redirect('home')
    response.delete_cookie('username')
    logout(request)
    return response


@login_required(login_url='login_user')
def d_like_post(request,destination):
    result=''
    destinationObj = get_object_or_404(Destination,destination_id=destination)
    if(destinationObj.userLike.filter(id=request.user.id)).exists():
        destinationObj.userLike.remove(request.user)
        destinationObj.likes-=1
        result=destinationObj.likes
        destinationObj.save()
    else:
        destinationObj.userLike.add(request.user)
        destinationObj.likes += 1
        result=destinationObj.likes
        destinationObj.save()

    return HttpResponse(result)

@login_required(login_url='login_user')
def d_dislike_post(request,destination):
    result = ''
    destinationObj = get_object_or_404(Destination, destination_id=destination)
    if (destinationObj.userDislike.filter(id=request.user.id)).exists():
        destinationObj.userDislike.remove(request.user)
        destinationObj.dislikes -= 1
        result = destinationObj.dislikes
        destinationObj.save()
    else:
        destinationObj.userDislike.add(request.user)
        destinationObj.dislikes += 1
        result = destinationObj.dislikes
        destinationObj.save()
    return HttpResponse(result)

@login_required(login_url='login_user')
def d_check_like(request,destination):
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (destination_obj.userLike.filter(id=request.user.id)).exists():
        return HttpResponse(1);
    else:
       return HttpResponse(0);
@login_required(login_url='login_user')
def d_check_dislike(request,destination):
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (destination_obj.userDislike.filter(id=request.user.id)).exists():
        return HttpResponse(1);
    else:
       return HttpResponse(0);

@login_required(login_url='login_user')
def a_check_like(request,attraction):
    attraction_obj = get_object_or_404(Attraction, attraction_id=attraction)
    if (attraction_obj.userLike.filter(id=request.user.id)).exists():
        return HttpResponse(1);
    else:
       return HttpResponse(0);
@login_required(login_url='login_user')
def a_check_dislike(request,attraction):
    attraction_obj = get_object_or_404(Attraction, attraction_id=attraction)
    if (attraction_obj.userDislike.filter(id=request.user.id)).exists():
        return HttpResponse(1);
    else:
       return HttpResponse(0);


@login_required(login_url='login_user')
def like_post(request,attraction):
    result=''
    attraction2 = get_object_or_404(Attraction,attraction_id=attraction)
    if(attraction2.userLike.filter(id=request.user.id)).exists():
        attraction2.userLike.remove(request.user)
        attraction2.likes-=1
        result=attraction2.likes
        attraction2.save()
    else:
        attraction2.userLike.add(request.user)
        attraction2.likes += 1
        result=attraction2.likes
        attraction2.save()

    return HttpResponse(result)

@login_required(login_url='login_user')
def dislike_post(request,attraction):
    result = ''
    attraction2 = get_object_or_404(Attraction, attraction_id=attraction)
    if (attraction2.userDislike.filter(id=request.user.id)).exists():
        attraction2.userDislike.remove(request.user)
        attraction2.dislikes -= 1
        result = attraction2.dislikes
        attraction2.save()
    else:
        attraction2.userDislike.add(request.user)
        attraction2.dislikes += 1
        result = attraction2.dislikes
        attraction2.save()
    return HttpResponse(result)

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
    Destinations = Destination.objects.order_by('-click_count')[:3]
    Attractions = Attraction.objects.order_by('-click_count')[:3]
    Recommendations = Recommendation.objects.all()[:3]
    context_home = {'Destinations': Destinations, 'Attractions': Attractions, 'Recommendations': Recommendations}
    return render(request, 'home.html', context_home)


def destination_list(request):
    Destinations = Destination.objects.all().order_by("-click_count")
    return render(request, 'destinations.html', {'Destinations': Destinations})


def attraction_list(request):
    Attractions = Attraction.objects.all().order_by("-click_count")
    city_list = []
    for attraction in Attractions:
        if attraction.city.name not in city_list:
            city_list.append(attraction.city.name)
    return render(request, 'attractions.html', {'Attractions': Attractions, 'city_list': city_list})


def detailed_destination(request, destination):
    city = Destination.objects.get(destination_id=destination)
    city.click_count += 1
    city.save()
    comments = city.destinationcomment_set.all().order_by('-created_time')
    if request.method == 'POST':
        add_comment = request.POST.get('add_comment')
        DestinationComment.objects.create(
            user=request.user,
            comment_on=city,
            comment_content=add_comment
        )
    return render(request, "destination_detail.html", {'city': city, 'comments': comments})


def detailed_attraction(request, attraction):
    place = Attraction.objects.get(attraction_id=attraction)
    place.click_count += 1
    place.save()
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
    # context = {'comment': comment, 'city': city}
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
        cities = Destination.objects.all().order_by("name")
    else:
        cities = Destination.objects.filter(stateCode=state).order_by("name")
    return render(request, "search_result.html", {'cities': cities, 'match': match})


def filter_city(request):
    city = ''
    match = True
    if request.method == 'GET':
        city = request.GET.get('city')

    if city == 'CITY':
        places = Attraction.objects.all().order_by("name")
    else:
        places = Attraction.objects.filter(city__name=city).order_by("name")
    return render(request, "search_result.html", {'places': places, 'match': match, 'city': city})


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comment_on']


class AttractionCommentModelViewSet(viewsets.ModelViewSet):
    serializer_class = AttractionCommentSerializer
    queryset = AttractionComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comment_on']

class RecommendationModelViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()

