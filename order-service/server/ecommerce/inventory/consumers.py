from ecommerce.celery import ProductAddConsumer


class UpdateInventory(ProductAddConsumer):
    def process_message(self, body, message):
        from inventory import models

        models.ProductInventory(product_id=1, count=10).save()
        message.ack()