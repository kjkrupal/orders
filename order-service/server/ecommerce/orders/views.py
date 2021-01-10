from django.db import transaction
from rest_framework import viewsets, mixins, status, response, exceptions

from . import serializers, models


class OrderViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data.get("product")

        if product.count < 1:
            error = {"message": "Product is no longer available, check back later!"}
            return response.Response(data=error, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            product.count -= 1
            product.save()

            order_details = models.OrderDetails.objects.create(
                **serializer.validated_data.get("order_details")
            )

            order = models.Order.objects.create(
                product=product,
                order_details=order_details,
                status=models.Order.CREATED,
            )

        response_serializer = self.get_serializer(order)

        headers = self.get_success_headers(serializer.data)
        return response.Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
