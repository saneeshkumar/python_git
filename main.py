import data_set

data_set.create_user_details()
data_set.create_item_details()

order_list=[]

for order_id in range(0,100):
	order_list.append(data_set.create_order(order_id))
	order_json = order_list[order_id].create_json()
	print(order_json)