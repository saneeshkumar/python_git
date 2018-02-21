import data_set
import time
import json

from boto import kinesis

KINESIS_STREAM_NAME = 'kinesis_test_stream'
SHARD_ID = 'shardId-000000000000'

data_set.create_user_details()
data_set.create_item_details()

kinesis = kinesis.connect_to_region("ap-northeast-1")

records=[];

for order_id in range(0,200):
	order = data_set.create_order(order_id)
	order_json=order.create_json()
	record = {'Data': json.dumps(order_json),'PartitionKey': str(hash(order.user_details.first_name))}
	records.append(record)
	if order_id%10 == 0:
		kinesis.put_records(records, KINESIS_STREAM_NAME)
		records=[];

#shard_iter = kinesis.get_shard_iterator(KINESIS_STREAM_NAME, SHARD_ID, "LATEST")["ShardIterator"]
#while 1==1:
#	out = kinesis.get_records(shard_iter, limit=2)
#	shard_iter = out["NextShardIterator"]
#	print (out)
#	time.sleep(0.2)