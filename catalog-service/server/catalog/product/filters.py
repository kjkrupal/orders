from django.db.models import Q

from django_filters.rest_framework import CharFilter, FilterSet

from .models import Product


class ProductFilterSet(FilterSet):
    query = CharFilter(method="filter_query")

    def filter_query(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

    class Meta:
        model = Product
        fields = ("name",)
