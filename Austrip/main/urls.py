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
    path('destinations/', views.destination, name="destination_list"),
    path('attractions/', views.attraction, name="attraction_list"),
    path('<name>', views.detailed_item, name="item_details"),
    path('accounts/', include('accounts.urls')),
    path('destination_detail/', views.destination_detail, name="destination_detail"),
    path('detail_destination/', views.detail_destination, name="detail_destination"),
    path('viewset/', include(apiRouter.urls)),
]
