from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from projects.models import Client


class ClientFilter(FilterSet):
    name_contains = CharFilter(field_name='name', lookup_expr='icontains')
    name_starts_with = CharFilter(field_name='name', lookup_expr='istartswith')

    class Meta:
        model = Client
        fields = ['name', ]
