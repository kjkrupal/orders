from django.contrib import admin

from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "name",
        "quantity",
    )
    list_display = (
        "id",
        "name",
        "quantity",
    )
    list_filter = ("name",)
    ordering = ("id",)
    readonly_fields = ("id",)
