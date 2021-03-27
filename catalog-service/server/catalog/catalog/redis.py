import json
import redis

redis_client = redis.StrictRedis(host="redis", port=6379, db=1, password="pAssw0rd")


def publish_data_on_redis(data, channel):
    redis_client.publish(channel, json.dumps(data))