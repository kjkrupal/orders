from django.contrib import admin

from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('id','key', 'country', 'description', 'points', 'price', 'variety', 'winery',)
    list_display = ('id','key', 'country', 'points', 'price', 'variety', 'winery',)
    list_filter = ('country', 'variety', 'winery',)
    ordering = ('id','key',)
    readonly_fields = ('id','key',) 
