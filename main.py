import order_details

order_status = order_details.OrderStatus()
user = order_details.UserDetails("1", "Saneesh", "Kumar", "22-6-106")
item = order_details.ItemDetails("1", "iphoneX", "black", 100000)
order = order_details.OrderDetails( "1", user, item, order_status.New, 3)

order_json = order.create_json()

print(order_json)
