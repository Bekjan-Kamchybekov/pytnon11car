from django_filters.rest_framework import FilterSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['gt', 'lt'],
            'year': ['gt', 'lt'],
            'mileage': ['gt', 'lt'],
        }

class CarSearch(SearchFilter):
    class Meta:
        model = Car
        fields = {
            'car_name': ['exact'],
            'region_or_city': ['exact'],
        }
