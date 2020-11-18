from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .decorators import *
from .forms import CreateUserForm, ChangeUserInfo, ChangePicBio, EditRecommendation, AddCommentAttraction, \
    AddCommentDestination
from .serializers import *
from django.http import HttpResponse, JsonResponse


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
def profile_a_bookmarks(request):
    user_obj = get_object_or_404(UserInfo, user=request.user.id)
    a_book = user_obj.attraction_bookmark.all()
    all_pro = a_book.values('name', 'image', 'attraction_id')
    return JsonResponse(list(all_pro), safe=False)


@login_required(login_url='login_user')
def profile_d_bookmarks(request):
    user_obj = get_object_or_404(UserInfo, user=request.user.id)
    d_book = user_obj.destination_bookmark.all()
    all_pro = d_book.values('name', 'image', 'destination_id')
    return JsonResponse(list(all_pro), safe=False)


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


# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid:
#             user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
#             # user = form.get_user
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Invalid username or password :(')
#     else:
#         form = AuthenticationForm()
#     context = {'form': form}
#     return render(request, 'login_restyled.html', context)
#

def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password :(')
    return render(request, 'login_restyled.html')
    # return render(request, 'login_restyled.html')


def logout_user(request):
    response = redirect('home')
    logout(request)
    return response


@login_required(login_url='login_user')
def d_like_post(request, destination):
    result = ''
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (destination_obj.userLike.filter(id=request.user.id)).exists():
        destination_obj.userLike.remove(request.user)
        destination_obj.likes -= 1
        result = destination_obj.likes
        destination_obj.save()
    else:
        destination_obj.userLike.add(request.user)
        destination_obj.likes += 1
        result = destination_obj.likes
        destination_obj.save()

    return HttpResponse(result)


@login_required(login_url='login_user')
def d_dislike_post(request, destination):
    result = ''
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (destination_obj.userDislike.filter(id=request.user.id)).exists():
        destination_obj.userDislike.remove(request.user)
        destination_obj.dislikes -= 1
        result = destination_obj.dislikes
        destination_obj.save()
    else:
        destination_obj.userDislike.add(request.user)
        destination_obj.dislikes += 1
        result = destination_obj.dislikes
        destination_obj.save()
    return HttpResponse(result)


@login_required(login_url='login_user')
def d_check_like(request, destination):
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (destination_obj.userLike.filter(id=request.user.id)).exists():
        return HttpResponse("#008000")
    else:
        return HttpResponse("#a9a9a9")


@login_required(login_url='login_user')
def d_check_dislike(request, destination):
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (destination_obj.userDislike.filter(id=request.user.id)).exists():
        return HttpResponse("#ff0000")
    else:
        return HttpResponse("#a9a9a9")


@login_required(login_url='login_user')
def a_check_like(request, attraction):
    attraction_obj = get_object_or_404(Attraction, attraction_id=attraction)
    if (attraction_obj.userLike.filter(id=request.user.id)).exists():
        return HttpResponse("#008000")
    else:
        return HttpResponse("#a9a9a9")


@login_required(login_url='login_user')
def a_check_dislike(request, attraction):
    attraction_obj = get_object_or_404(Attraction, attraction_id=attraction)
    if (attraction_obj.userDislike.filter(id=request.user.id)).exists():
        return HttpResponse("#ff0000")
    else:
        return HttpResponse("#a9a9a9")


@login_required(login_url='login_user')
def a_check_bookmark(request, attraction):
    user_obj = get_object_or_404(UserInfo, user=request.user.id)
    if (user_obj.attraction_bookmark.filter(attraction_id=attraction)).exists():
        return HttpResponse("#daa520")
    else:
        return HttpResponse("#a9a9a9")


@login_required(login_url='login_user')
def d_check_bookmark(request, destination):
    user_obj = get_object_or_404(UserInfo, user=request.user.id)
    if (user_obj.destination_bookmark.filter(destination_id=destination)).exists():
        return HttpResponse("#daa520")
    else:
        return HttpResponse("#a9a9a9")


@login_required(login_url='login_user')
def d_bookmark(request, destination):
    user_obj = get_object_or_404(UserInfo, user=request.user.id)
    destination_obj = get_object_or_404(Destination, destination_id=destination)
    if (user_obj.destination_bookmark.filter(destination_id=destination)).exists():
        user_obj.destination_bookmark.remove(destination_obj)
        user_obj.save()
        return HttpResponse("#a9a9a9")
    else:
        user_obj.destination_bookmark.add(destination_obj)
        user_obj.save()
        return HttpResponse("#daa520")


@login_required(login_url='login_user')
def a_bookmark(request, attraction):
    user_obj = get_object_or_404(UserInfo, user=request.user.id)
    attraction_obj = get_object_or_404(Attraction, attraction_id=attraction)
    if (user_obj.attraction_bookmark.filter(attraction_id=attraction)).exists():
        user_obj.attraction_bookmark.remove(attraction_obj)
        user_obj.save()
        return HttpResponse("#a9a9a9")
    else:
        user_obj.attraction_bookmark.add(attraction_obj)
        user_obj.save()
        return HttpResponse("#daa520")


@login_required(login_url='login_user')
def like_post(request, attraction):
    result = ''
    attraction2 = get_object_or_404(Attraction, attraction_id=attraction)
    if (attraction2.userLike.filter(id=request.user.id)).exists():
        attraction2.userLike.remove(request.user)
        attraction2.likes -= 1
        result = attraction2.likes
        attraction2.save()
    else:
        attraction2.userLike.add(request.user)
        attraction2.likes += 1
        result = attraction2.likes
        attraction2.save()

    return HttpResponse(result)


@login_required(login_url='login_user')
def dislike_post(request, attraction):
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
    return render(request, 'signup_restyled.html', {'form': form})


def home(request):
    destinations = Destination.objects.order_by('-click_count')[:3]
    attractions = Attraction.objects.order_by('-click_count')[:3]
    recommendations = Recommendation.objects.all()[:3]
    context_home = {'Destinations': destinations, 'Attractions': attractions, 'Recommendations': recommendations}
    return render(request, 'home.html', context_home)


def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'Destinations': destinations})


def attraction_list(request):
    attractions = Attraction.objects.all()
    city_list = []
    for attraction in attractions:
        if attraction.city.name not in city_list:
            city_list.append(attraction.city.name)
    return render(request, 'attractions.html', {'Attractions': attractions, 'city_list': city_list})


def detailed_destination(request, destination):
    city = get_object_or_404(Destination, destination_id=destination)
    city.click_count += 1
    city.save()
    comments = city.destinationcomment_set.all()
    add_form = AddCommentDestination()
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


def edit_comment_destination(request, comment_id, destination):
    city = Destination.objects.get(destination_id=destination)
    comment = DestinationComment.objects.get(commentId=comment_id)
    if request.method == 'POST':
        edit_form = AddCommentDestination(request.POST, instance=comment)
        if edit_form.is_valid:
            edit_form.save()
            url = 'http://127.0.0.1:8000/destinations/' + city.destination_id + '/'
            return redirect(url)
    else:
        edit_form = AddCommentDestination(instance=comment)
    context = {'form': edit_form, 'city': city, 'comment': comment}
    return render(request, 'edit_destination.html', context)


def delete_comment_attraction(request, comment_id, attraction):
    place = Attraction.objects.get(attraction_id=attraction)
    comments = place.attractioncomment_set.all()
    comment = AttractionComment.objects.get(commentId=comment_id)
    comment.delete()
    context = {'comments': comments, 'comment': comment, 'place': place}
    return render(request, 'attraction_detail.html', context)


def edit_comment_attraction(request, comment_id, attraction):
    place = Attraction.objects.get(attraction_id=attraction)
    comment = AttractionComment.objects.get(commentId=comment_id)
    if request.method == 'POST':
        edit_form = AddCommentAttraction(request.POST, instance=comment)
        if edit_form.is_valid:
            edit_form.save()
            url = 'http://127.0.0.1:8000/attractions/' + place.attraction_id + '/'
            return redirect(url)
    else:
        edit_form = AddCommentAttraction(instance=comment)
    context = {'form': edit_form, 'place': place, 'comment': comment}
    return render(request, 'edit_attraction.html', context)


def delete_comment_destination(request, comment_id, destination):
    city = Destination.objects.get(destination_id=destination)
    comment = DestinationComment.objects.get(commentId=comment_id)
    comments = city.destinationcomment_set.all()
    comment.delete()
    context = {'comments': comments, 'comment': comment, 'city': city}
    return render(request, 'destination_detail.html', context)


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
