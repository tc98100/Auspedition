from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'


class DestinationCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationComment
        fields = '__all__'


class AttractionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionComment
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'
