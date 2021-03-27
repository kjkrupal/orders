# Add subscriber here
from . import models

import json


def update_inventory(data):
    inventory_data = json.loads(data)
    try:
        inventory = models.ProductInventory.get(product_id=inventory_data["product_id"])
    except models.ProductInventory.DoesNotExist:
        inventory = models.ProductInventory(product_id=inventory_data["product_id"])
    inventory.quantity = inventory_data["quantity"]
    inventory.save()