from __future__ import absolute_import, unicode_literals

# Standard Library
import os
import abc

import kombu

from . import constants
from celery import Celery, bootsteps

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

app = Celery("ecommerce")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# setting publisher
with app.pool.acquire(block=True) as conn:
    exchange = kombu.Exchange(
        name=constants.EXCHANGE_NAME,
        channel=conn,
    )

    order_create_catalog_queue = kombu.Queue(
        name=constants.ORDER_CREATE_CATALOG_QUEUE,
        exchange=exchange,
        channel=conn,
    )
    order_create_analytics_queue = kombu.Queue(
        name=constants.ORDER_CREATE_ANALYTICS_QUEUE,
        exchange=exchange,
        channel=conn,
    )
    order_create_processor_queue = kombu.Queue(
        name=constants.ORDER_CREATE_PROCESSOR_QUEUE,
        exchange=exchange,
        channel=conn,
    )
    product_add_queue = kombu.Queue(
        name=constants.PRODUCT_ADD_QUEUE,
        exchange=exchange,
        channel=conn,
    )


# setting consumer
class ProductAddConsumer(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [
            kombu.Consumer(
                channel,
                queues=[product_add_queue],
                callbacks=[self.process_message],
                accept=["json"],
            )
        ]

    @abc.abstractmethod
    def process_message(self, body, message):
        pass


app.steps["consumer"].add(ProductAddConsumer)