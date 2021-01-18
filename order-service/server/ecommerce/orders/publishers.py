from __future__ import absolute_import, unicode_literals

from celery import shared_task

from ecommerce import constants as project_constants
from ecommerce.celery import app


@shared_task
def order_created(order):
    with app.producer_pool.acquire(block=True) as producer:
        producer.publish(
            order,
            exchange=project_constants.EXCHANGE_NAME,
        )