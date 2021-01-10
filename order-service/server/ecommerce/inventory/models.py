from django.db import models


class ProductInventory(models.Model):
    product_id = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return f"{self.id}"
