# filters.py
import django_filters
from .models import Organization

class OrganizationFilter(django_filters.FilterSet):
    class Meta:
        model = Organization
        fields = {
            'name': ['icontains'],
            'domain': ['icontains'],
            'year_founded': ['exact'],
            'industry': ['icontains'],
            'size_range': ['icontains'],
            'locality': ['icontains'],
            'country': ['icontains'],
        }
