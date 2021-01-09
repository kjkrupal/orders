from django.contrib import admin

from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "product",
        "tracking_id",
        "status",
        "order_details",
        "created_ts",
        "last_status_update_ts",
    )
    list_display = (
        "id",
        "product",
        "tracking_id",
        "status",
    )
    ordering = ("id",)
    readonly_fields = (
        "id",
        "product",
        "tracking_id",
        "status",
        "order_details",
        "created_ts",
        "last_status_update_ts",
    )


@admin.register(models.OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    fields = (
        "id",
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
        "first_name",
        "last_name",
        "city",
    )
    ordering = ("id",)
    readonly_fields = (
        "id",
        "first_name",
        "last_name",
        "street_1",
        "street_2",
        "city",
        "state",
        "zip_code",
    )
