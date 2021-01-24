from django.db.models import Q

from django_filters.rest_framework import CharFilter, FilterSet

from .models import Product

class ProductFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(variety__contains=value) |
            Q(winery__contains=value) |
            Q(description__contains=value)
        )
        return queryset.filter(search_query)

    class Meta:
        model = Product
        fields = ('query', 'country', 'points',)
