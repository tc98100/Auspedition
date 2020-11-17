from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect,get_object_or_404
from rest_framework import viewsets
from django.db.models import Q,F
from .decorators import *
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from .forms import CreateUserForm, ChangeUserInfo
from .models import *
from .serializers import *


@login_required(login_url='login_user')
def profile(request):
    return render(request, "profile.html")


@login_required(login_url='login_user')
def profile_change(request):
    user = request.user.userinfo
    form = ChangeUserInfo(instance=user)
    return render(request, "profile_change.html", {'form': form})


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

            group = Group.objects.get(name='user')
            new_user.groups.add(group)

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
    return render(request, "destination_detail.html", {'city': city, 'comments': comments})


def detailed_attraction(request, attraction):
    place = Attraction.objects.get(attraction_id=attraction)
    comments = place.attractioncomment_set.all()
    return render(request, "attraction_detail.html", {'place': place, 'comments': comments})


def detailed_recommendation(request, recommendation):
    specific_recommendation = Recommendation.objects.get(recommendation_id=recommendation)
    return render(request, "recommendation.html", {'recommendation': specific_recommendation})


def recommendation_edit(request, recommendation):
    specific_recommendation = Recommendation.objects.get(recommendation_id=recommendation)
    return render(request, "staff_recommendation.html", {'recommendation': specific_recommendation})


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

