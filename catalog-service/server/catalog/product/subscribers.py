import json

from . import models


def order_created(data):
    product_data = json.loads(data)
    try:
        product = models.Product.objects.get(id=product_data["product_id"])
        product.quantity = product_data["quantity"]
        product.save()
    except models.Product.DoesNotExist:
        pass