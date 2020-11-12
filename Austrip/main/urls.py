from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import DestinationModelViewSet, AttractionModelViewSet, DestinationCommentModelViewSet, \
    AttractionCommentModelViewSet, RecommendationModelViewSet, UserModelViewSet

apiRouter = DefaultRouter()
apiRouter.register('destination', DestinationModelViewSet, basename='destination')
apiRouter.register('attraction', AttractionModelViewSet, basename='attraction')
apiRouter.register('destinationComment', DestinationCommentModelViewSet, basename='destinationComment')
apiRouter.register('attractionComment', AttractionCommentModelViewSet, basename='destinationComment')
apiRouter.register('user', UserModelViewSet, basename='user')
apiRouter.register('recommendation', RecommendationModelViewSet, basename='recommendation')

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destination_list, name="destination_list"),
    path('attractions/', views.attraction_list, name="attraction_list"),
    path('destinations/<str:destination>/', views.detailed_destination, name="destination_details"),
    path('attractions/<str:attraction>/', views.detailed_attraction, name="attraction_details"),
    path('recommendations/<str:recommendation>/', views.detailed_recommendation, name="recommendation_details"),


    path('result/', views.search_result, name="search_result"),

    # temporary use, needs to be changed
    path('profile/', views.profile, name="profile"),

    path('viewset/', include(apiRouter.urls)),
]
