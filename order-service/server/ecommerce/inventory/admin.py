from django.contrib import admin

from . import models


@admin.register(models.ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "product_id",
        "count",
    )
    list_display = (
        "id",
        "product_id",
        "count",
    )
    ordering = ("id",)
    readonly_fields = (
        "id",
        "product_id",
    )
