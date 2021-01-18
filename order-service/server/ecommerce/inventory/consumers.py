from ecommerce.celery import ProductAddConsumer


class UpdateInventory(ProductAddConsumer):
    def process_message(self, body, message):
        pass