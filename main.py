import data_set
import time
import json
import os
import boto

from boto import kinesis
from boto.s3.key import Key


ORDER_DATA_LOCATION = './order_details/'

KINESIS_STREAM_NAME = 'kinesis_test_stream'
SHARD_ID = 'shardId-000000000000'

S3_BUCKET_NAME = 'pp-s3-landing'

data_set.create_user_details()
data_set.create_item_details()

if not os.path.exists(ORDER_DATA_LOCATION):
    os.makedirs(ORDER_DATA_LOCATION)

s3_connection = boto.connect_s3()
bucket = s3_connection.get_bucket(S3_BUCKET_NAME)

kinesis = kinesis.connect_to_region("ap-northeast-1")

records = [];

for order_id in range(0, 10):
    order = data_set.create_order(order_id)
    order_json = order.create_json()
    file_name = 'order-{order_id}.json'.format(path=ORDER_DATA_LOCATION, order_id=order.id)
    bucket_key = Key(bucket)
    bucket_key.key = file_name
    bucket_key.set_contents_from_string(order_json)


