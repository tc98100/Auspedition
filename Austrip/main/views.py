from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination, Attraction, DestinationComment, AttractionComment, Recommendation


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
