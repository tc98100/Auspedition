from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Q
from .models import *
from .serializers import *
from .search import *


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
    return render(request, 'attractions.html', {'Attractions': Attractions})


def detailed_destination(request, destination):
    city = Destination.objects.get(destination_id=destination)
    return render(request, "destination_detail.html", {'city': city})


def detailed_attraction(request, attraction):
    place = Attraction.objects.get(attraction_id=attraction)
    return render(request, "attraction_detail.html", {'place': place})


def detailed_recommendation(request, recommendation):
    specific_recommendation = Recommendation.objects.get(recommendation_id=recommendation)
    return render(request, "recommendation.html", {'recommendation': specific_recommendation})


def search_result(request):
    user_input = ''
    match = True

    if request.method == 'GET':
        user_input = request.GET.get('input')

    condition1 = Q(name__icontains=user_input) | Q(stateCode__icontains=user_input) | Q(state__icontains=user_input)
    condition2 = Q(name__icontains=user_input) | Q(city__icontains=user_input) | Q(state__icontains=user_input) | \
                 Q(stateCode__icontains=user_input)

    result_destination = Destination.objects.filter(condition1)
    result_attraction = Attraction.objects.filter(condition2)

    if not result_destination and not result_attraction:
        match = False
        result_destination = Destination.objects.all()[:3]
        result_attraction = Attraction.objects.all()[:3]

    context = {'cities': result_destination, 'places': result_attraction, 'match': match}
    return render(request, "search_result.html", context)


def filter_state(request):
    state = ''
    if request.method == 'GET':
        state = request.GET.get('state')

    if state == 'STATE':
        cities = Destination.objects.all()
    else:
        cities = Destination.objects.filter(stateCode=state)
    return render(request, "search_result.html", {'cities': cities})


def filter_city(request):
    city = ''
    if request.method == 'GET':
        city = request.GET.get('city')

    if city == 'CITY':
        places = Attraction.objects.all()
    else:
        places = Attraction.objects.filter(name=city)
    return render(request, "search_result.html", {'places': places})


# temporary
def profile(request):
    return render(request, "profile.html")


def profile_change(request):
    return render(request, "profile_change.html")


####


# def count_increment_dest(destination):
#     city = Destination.objects.get(destination_id=destination)
#     city.click_count += 1
#     city.save(update_fields=['click_field'])


class DestinationModelViewSet(viewsets.ModelViewSet):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


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
