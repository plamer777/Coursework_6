"""This file contains AdFilter class providing functionality to filter
queryset by demanded filters"""
from django_filters import filters, rest_framework
from ads.models import Ad
# ------------------------------------------------------------------------


class AdFilter(rest_framework.FilterSet):
    """AdFilter class serves to filter Ad objects by text contained in the
    title field"""
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ['title']
