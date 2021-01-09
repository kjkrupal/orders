from rest_framework import serializers

from . import models


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            "tracking_id",
            "status",
            "created_ts",
            "last_status_update_ts",
        )


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderDetails
        read_only_fields = ("id",)
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


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailsSerializer()

    class Meta:
        model = models.Order
        fields = (
            "id",
            "product",
            "tracking_id",
            "order_details",
        )
        read_only_fields = (
            "id",
            "tracking_id",
            "status",
        )
        extra_kwargs = {
            "order_details": {"write_only": True},
            "product": {"write_only": True},
        }
