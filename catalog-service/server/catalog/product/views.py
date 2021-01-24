from django.shortcuts import render
from rest_framework.generics import ListAPIView

# Create your views here.
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilterSet


from .models import Product

class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet