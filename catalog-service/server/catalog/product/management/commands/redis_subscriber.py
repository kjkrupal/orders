# from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError

from catalog import constants

from catalog.product import subscribers

import json

import redis


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.StrictRedis(host="redis", port=6379, db=1, password="pAssw0rd")
        p = r.pubsub()
        p.psubscribe("order.*")
        print("Subscribed to topic........")
        for message in p.listen():
            if message["channel"].decode() == constants.ORDER_CREATE:
                subscribers.order_created(data=message["data"])
        print("Closing..........")