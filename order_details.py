import json

class OrderStatus:
	def __init__(self):
		self.New			= "New"
		self.Processing		= "Processing"
		self.Shipped		= "Shipped"
		self.Delivered		= "Delivered"
		self.Returned		= "Returned"
		self.Closed			= "Closed"

class UserDetails:
	def __init__(self, u_id, first_name, second_name, address):
		self.id				= u_id
		self.first_name		= first_name
		self.second_name	= second_name
		self.address		= address

	def create_json(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=False)

class ItemDetails:
	def __init__(self, item_id, name, color, price):
		self.id				= item_id
		self.name			= name
		self.color			= color
		self.price			= price

	def create_json(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=False)

class OrderDetails:
	def __init__(self, order_id, user_details, item_details, status, count):
		self.id				= order_id
		self.user_details	= user_details
		self.item_details	= item_details
		self.status			= status
		self.count			= count
		self.cost			= count * item_details.price

	def create_json(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=False)