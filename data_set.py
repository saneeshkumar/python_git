import order_details
import random

NUM_USERS = 10
NUM_ITEMS = 5

user_details=[]
product_details=[]

products = ["iphoneX", "iphone8+", "iphone8", "iphone7+", "iphone7"]
colors=[ "Jet Black", "Black", "Silver", "Gold", "Rose Gold" ]
product_price = [140184, 115344, 103464, 74800, 61800]

user_names=[
	"Rani Faltin", "Nadine Cremins",
	"Sadella Playden", "Fanya Lockhead",
	"Claudianus Sulter", "Graig Kobelt",
	"Desirae Lanfare", "Almira Dewing",
	"Caryl Heugle ", "Jeanette Saffen"]

user_address=[
	"0704 American Ash Terrace", "3 Stone Corner Trail",
	"8789 Garrison Drive", "07 Mallory Hill",
	"5 Service Pass", "47 American Place",
	"2 Katie Center", "9 Nova Terrace",
	"38850 Clemons Circle", "4212 Brickson Park Hill"]

def create_user_details():
	for u_id in range(0,NUM_USERS):
		names = str.split(user_names[u_id])
		user_details.append(order_details.UserDetails(u_id+1, names[0], names[1], user_address[u_id]))

def create_item_details():
	for u_id in range(0,NUM_ITEMS):
		product_details.append(order_details.ItemDetails(u_id+1, products[u_id], colors[u_id], product_price[u_id]))

def create_order(order_id):
	random_uid = random.randint(0,NUM_USERS-1)
	random_pid = random.randint(0,NUM_ITEMS-1)
	order_count = random.randint(1,5)
	order_status = order_details.OrderStatus()

	order = order_details.OrderDetails( order_id, user_details[random_uid], product_details[random_pid], order_status.New, order_count)
	return order