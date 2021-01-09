from django.db import models

from inventory import models as inventory_models


class Order(models.Model):
    CREATED = "CREATED"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"
    PROCESSING = "PROCESSING"
    DELIVERED = "DELIVERED"
    STATUS_TYPES = (
        (CREATED, CREATED),
        (REJECTED, REJECTED),
        (ACCEPTED, ACCEPTED),
        (PROCESSING, PROCESSING),
        (DELIVERED, DELIVERED),
    )

    product = models.ForeignKey(
        inventory_models.ProductInventory, on_delete=models.SET_NULL, null=True
    )

    status = models.CharField(max_length=32, choices=STATUS_TYPES, db_index=True)

    created_ts = models.DateTimeField(blank=True, auto_now_add=True)

    last_status_update_ts = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return f"{self.id}##{self.product.product_id}"


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_1 = models.CharField(max_length=255, blank=False, null=False)
    street_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    zip_code = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.id}##{self.order.id}##{self.first_name}_{self.last_name}"
