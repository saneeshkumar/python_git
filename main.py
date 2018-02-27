import data_set
import time
import json
import os

ORDER_DATA_LOCATION = './order_details/'

from boto import kinesis

KINESIS_STREAM_NAME = 'kinesis_test_stream'
SHARD_ID = 'shardId-000000000000'

data_set.create_user_details()
data_set.create_item_details()

if not os.path.exists(ORDER_DATA_LOCATION):
    os.makedirs(ORDER_DATA_LOCATION)

kinesis = kinesis.connect_to_region("ap-northeast-1")

records = [];

for order_id in range(0, 200):
    order = data_set.create_order(order_id)
    order_json = order.create_json()
    file_name = '{path}order_{order_id}.json'.format(path = ORDER_DATA_LOCATION,order_id=order.id)
    order_file = open(file_name, "w+")
    order_file.write(order_json)
    # record = {'Data': json.dumps(order_json), 'PartitionKey': str(hash(order.user_details.first_name))}
    # records.append(record)
    # if order_id % 10 == 0:
    #     kinesis.put_records(records, KINESIS_STREAM_NAME)
    #     records = [];

# shard_iter = kinesis.get_shard_iterator(KINESIS_STREAM_NAME, SHARD_ID, "LATEST")["ShardIterator"]
# while 1 == 1:
#     out = kinesis.get_records(shard_iter, limit=2)
#     shard_iter = out["NextShardIterator"]
#     print(out)
#     time.sleep(0.2)
