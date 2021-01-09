from rest_framework import serializers

from . import models


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            "id",
            "status",
            "created_ts",
            "last_status_update_ts",
        )
