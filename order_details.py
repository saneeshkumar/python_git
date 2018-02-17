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
		json_str = "\t\t\"UserDetails\": {\n"
		json_str += "\t\t\t\"id\": \"" + str(self.id) + "\",\n"
		json_str += "\t\t\t\"first_name\": \"" + self.first_name + "\",\n"
		json_str += "\t\t\t\"second_name\": \"" + self.second_name + "\",\n"
		json_str += "\t\t\t\"address\": \"" + self.address + "\"\n"
		json_str += "\t\t}"
		return json_str

class ItemDetails:
	def __init__(self, item_id, name, color, price):
		self.id				= item_id
		self.name			= name
		self.color			= color
		self.price			= price

	def create_json(self):
		json_str = "\t\t\"ItemDetails\": {\n"
		json_str += "\t\t\t\"id\": \"" + str(self.id) + "\",\n"
		json_str += "\t\t\t\"name\": \"" + self.name + "\",\n"
		json_str += "\t\t\t\"color\": \"" + self.color + "\",\n"
		json_str += "\t\t\t\"price\": \"" + str(self.price) + "\"\n"
		json_str += "\t\t}"
		return json_str

class OrderDetails:
	def __init__(self, order_id, user_details, item_details, status, count):
		self.id				= order_id
		self.user_details	= user_details
		self.item_details	= item_details
		self.status			= status
		self.count			= count
		self.cost			= count * item_details.price

	def create_json(self):
		json_str = "{\n"
		json_str += "\t\"OrderDetails\": {\n"
		json_str += "\t\t\"order_id\": \"" + str(self.id) + "\",\n"
		json_str += self.user_details.create_json() + ",\n"
		json_str += self.item_details.create_json() + ",\n"
		json_str += "\t\t\"status\": \"" + self.status + "\",\n"
		json_str += "\t\t\"count\": \"" + str(self.count) + "\",\n"
		json_str += "\t\t\"cost\": \"" + str(self.cost) + "\"\n"
		json_str += "\t}\n"
		json_str+="}"
		return json_str