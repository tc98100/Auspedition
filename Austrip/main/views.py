from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Destination, Attraction, DestinationComment, AttractionComment, Recommendation
from .serializers import *
from .search import Search


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
    result_destination = Search(request.GET, queryset=Destination.objects.all())
    result_attraction = Search(request.GET, queryset=Attraction.objects.all())
    cities = result_destination.qs
    places = result_attraction.qs

    return render(request, "search_result.html", {'result': result_destination, 'cities': cities, 'places': places})

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

def detail_destination(request):
    return render(request, 'detailed_destination.html')


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

