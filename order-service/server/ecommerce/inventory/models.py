import uuid
from django.db import models


class ProductInventory(models.Model):
    product_id = models.UUIDField(editable=False, default=uuid.uuid4)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.product_id}"
