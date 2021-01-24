from django.contrib import admin

from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('keys', 'country', 'description', 'points', 'price', 'variety', 'winery',)
    list_display = ('keys', 'country', 'points', 'price', 'variety', 'winery',)
    list_filter = ('country', 'variety', 'winery',)
    ordering = ('variety',)
    readonly_fields = ('keys',) 
