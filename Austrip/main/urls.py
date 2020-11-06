from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destination, name="destination_list"),
    path('attractions/', views.attraction, name="attraction_list"),
    path('<name>', views.detailed_item, name="item_details"),
    path('accounts/', include('accounts.urls'))
]