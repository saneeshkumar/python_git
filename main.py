import order_details
import json

order_status = order_details.OrderStatus()
user = order_details.UserDetails("1", "Saneesh", "Kumar", "22-6-106")
item = order_details.ItemDetails("1", "iphoneX", "black", 100000)
order = order_details.OrderDetails( "1", user, item, order_status.New, 3)


#json_sample = json.dumps(order.__dict__)


#with open('data.txt', 'w') as outfile:
 #   json.dump(data, outfile)