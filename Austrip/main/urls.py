from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import *

apiRouter = DefaultRouter()
apiRouter.register('destination', DestinationModelViewSet, basename='destination')
apiRouter.register('attraction', AttractionModelViewSet, basename='attraction')
apiRouter.register('destinationComment', DestinationCommentModelViewSet, basename='destinationComment')
apiRouter.register('attractionComment', AttractionCommentModelViewSet, basename='attractionComment')
apiRouter.register('user', UserModelViewSet, basename='user')
apiRouter.register('recommendation', RecommendationModelViewSet, basename='recommendation')

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destination_list, name="destination_list"),
    path('attractions/', views.attraction_list, name="attraction_list"),
    path('destinations/<str:destination>/', views.detailed_destination, name="destination_details"),
    path('attractions/<str:attraction>/', views.detailed_attraction, name="attraction_details"),

    path('recommendations/<str:recommendation>/', views.detailed_recommendation, name="recommendation_details"),
    path('recommendations/<str:recommendation>/edit/', views.edit, name="edit"),

    path('attractions/delete/<str:comment_id>', views.delete_comment_attraction, name='delete_comment_attraction'),
    path('attractions/edit/<str:comment_id>/', views.edit_comment_attraction, name='edit_comment_attraction'),

    path('destinations/delete/<str:comment_id>/', views.delete_comment_destination, name='delete_comment_destination'),
    path('destinations/edit/<str:comment_id>/', views.edit_comment_destination, name='edit_comment_destination'),

    path('search-result/', views.search_result, name="search_result"),
    path('destination-result/', views.filter_state, name="destination_result"),
    path('attraction-result/', views.filter_city, name="attraction_result"),

    # temporary use, needs to be changed
    path('profile/', views.profile, name="profile"),
    path('change-profile/', views.profile_change, name="change_profile"),

    path('viewset/', include(apiRouter.urls)),

    # user
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/change-password/', views.change_password, name='change_password'),

    path('profile/abookmark/',views.profile_a_bookmarks,name='a_profile_bookmark'),
    path('profile/dbookmark/', views.profile_d_bookmarks, name='d_profile_bookmark'),

    path('attractions/<str:attraction>/dislike/', views.dislike_post, name='dislike'),
    path('attractions/<str:attraction>/like/', views.like_post, name='like'),
    path('destinations/<str:destination>/like/', views.d_like_post, name='d_like'),
    path('destinations/<str:destination>/dislike/', views.d_dislike_post, name='d_dislike'),

    path('attractions/<str:attraction>/checkDislike/', views.a_check_dislike, name='a_check_dislike'),
    path('attractions/<str:attraction>/checkLike/', views.a_check_like, name='a_check_like'),
    path('destinations/<str:destination>/checkDislike/', views.d_check_dislike, name='d_check_dislike'),
    path('destinations/<str:destination>/checkLike/', views.d_check_like, name='d_check_like'),

    path('destinations/<str:destination>/checkBookmark/', views.d_check_bookmark, name='d_check_bookmark'),
    path('attractions/<str:attraction>/checkBookmark/', views.a_check_bookmark, name='a_check_bookmark'),

    path('destinations/<str:destination>/bookmark/', views.d_bookmark, name='d_bookmark'),
    path('attractions/<str:attraction>/bookmark/', views.a_bookmark, name='a_bookmark'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)