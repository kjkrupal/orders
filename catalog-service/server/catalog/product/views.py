from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.http import JsonResponse
from django.views import View

from .models import Product

class ProductView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query','')
        country = self.request.GET.get('country', '')
        points = self.request.GET.get('points', '')

        if any([query,country,points]):
            search_query = Q(
                Q(variety__contains=query) |
                Q(winery__contains=query) |
                Q(description__contains=query)
            )
            if country:
                search_query &= Q(country=country)
            if points:
                search_query &= Q(points=int(points))
            
            products = Product.objects.filter(search_query)
        else:
            products = Product.objects.none()
        
        return JsonResponse(data = [{
            'keys': product.keys,
            'country': product.country,
            'description': product.description,
            'points': product.points,
            'price': product.price,
            'variety': product.variety,
            'winery': product.winery,
        } for product in products], safe=False)

