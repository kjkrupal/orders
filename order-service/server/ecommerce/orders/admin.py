from django.contrib import admin

from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "product",
        "status",
    )
    list_display = (
        "id",
        "product",
        "status",
    )
    ordering = ("id",)
    readonly_fields = (
        "id",
        "product",
        "status",
    )


@admin.register(models.OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "order",
        "first_name",
        "last_name",
        "street_1",
        "street_2",
        "city",
        "state",
        "zip_code",
    )
    list_display = (
        "id",
        "order",
        "first_name",
        "last_name",
        "city",
    )
    ordering = ("id",)
    readonly_fields = ("id",)
