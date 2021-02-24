from __future__ import absolute_import, unicode_literals

import json

from celery import shared_task

from ecommerce import constants as project_constants
from ecommerce.celery import app

from . import serializers


@shared_task
def order_created(order):
    order_serializer = serializers.PublishOrderSerializer(order)
    order_data = json.dumps(order_serializer.data)
    with app.producer_pool.acquire(block=True) as producer:
        producer.publish(
            order_data,
            exchange=project_constants.EXCHANGE_NAME,
        )