import django_filters
from django_filters import *


from .models import Destination, Attraction

class Search(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='iexact')
    state = CharFilter(field_name='state', lookup_expr='iexact')

    class Meta:
        model = Destination
        fields = ''
