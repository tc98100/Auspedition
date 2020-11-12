import django_filters
from django_filters import *

from .models import Destination, Attraction

class Search(django_filters.FilterSet):

    state = CharFilter(field_name='state', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Destination
        fields = ''

