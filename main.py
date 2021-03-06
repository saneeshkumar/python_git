import data_set
import time
import json
import boto3

KINESIS = 'kinesis'
REGION_NAME ='ENTER_REGION_NAME'
STREAM_NAME = 'ENTER_STREAM_NAME'

data_set.create_user_details()
data_set.create_item_details()

kinesis_client = boto3.client(KINESIS, region_name=REGION_NAME)

def puts_to_stream():
	records=[]
	for order_id in range(0,5):
		order = data_set.create_order(order_id)
		order_json=order.create_json()
		record = {'Data': json.dumps(order_json),'PartitionKey': str(hash(order_id))}
		records.append(record)
	kinesis_client.put_records(Records=records, StreamName=STREAM_NAME)

def read_from_stream():
	stream_description = kinesis_client.describe_stream( StreamName=STREAM_NAME)
	shard_id = stream_description['StreamDescription']['Shards'][0]['ShardId']
	shard_iterator = kinesis_client.get_shard_iterator( StreamName=STREAM_NAME, ShardId=shard_id, ShardIteratorType='TRIM_HORIZON')
	records = kinesis_client.get_records( ShardIterator=shard_iterator['ShardIterator'], Limit=100)
	print (records)
	print ("-----------------------------")
	time.sleep(0.2)

	while records['MillisBehindLatest'] > 0:
		records = kinesis_client.get_records( ShardIterator=records['NextShardIterator'], Limit=100)
		print (records)
		print ("-----------------------------")
		time.sleep(0.2)


if __name__=='__main__':
	puts_to_stream()
	read_from_stream()