from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Destination, Attraction, DestinationComment, AttractionComment, Recommendation
from .serializers import *


def home(request):
    return render(request, 'home.html')

def destination(request):
    Destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'Destinations': Destinations})

def attraction(request):
    return render(request, 'attractions.html')

def profile(request):
    return render(request, 'profile.html')

def detailed_item(request, name):
    city = Destination.objects.get(destination_id=name)
    return render(request, "detailed_destination.html", {'city': city})

def destination_detail(request):
    return render(request, 'destination_detail.html')


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

