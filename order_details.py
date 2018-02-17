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

class ItemDetails:
	def __init__(self, item_id, name, color, price):
		self.id				= item_id
		self.name			= name
		self.color			= color
		self.price			= price

class OrderDetails:
	def __init__(self, order_id, user_details, item_details, order_status, order_count):
		self.order_id		= order_id
		self.user_details	= user_details
		self.item_details	= item_details
		self.order_status	= order_status
		self.order_count	= order_count
		self.order_cost		= order_count * item_details.price

	def create_json_order(self):
		return