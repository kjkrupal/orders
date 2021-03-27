# Add publisher here
from ecommerce import redis, constants


def order_created(order):
    order_details = {
        "product_id": order.product_id,
        "quantity": 1,
    }
    redis.publish_data_on_redis(
        data=order_details,
        channel=constants.ORDER_CREATE,
    )
