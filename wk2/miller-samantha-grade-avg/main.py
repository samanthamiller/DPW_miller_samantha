# Samantha Miller
# March 11, 2014
# Grade Average sike 

import webapp2
from detail import Detail
class MainHandler(webapp2.RequestHandler):
	def get(self):
		# Creates detail object
		detail = Detail()

		# Instantiate first bill
		table_1 = RestaurantBill()
		# Assign class's attributes
		table_1.tableNumber = 'Table 1'
		table_1.plate1 = 7.52
		table_1.plate2 = 3.67
		table_1.plate3 = 6.53
		table_1.plate4 = 8.96
		table_1.plate5 = 6.78

		# Instantiate second bill
		table_2 = RestaurantBill()
		# Assign class's attributes
		table_2.tableNumber = 'Table 2'
		table_2.plate1 = 8.95
		table_2.plate2 = 5.83
		table_2.plate3 = 3.99
		table_2.plate4 = 12.52
		table_2.plate5 = 14.78

		# Instantiate third bill
		table_3 = RestaurantBill()
		# Assign class's attributes
		table_3.tableNumber = 'Table 3'
		table_3.plate1 = 3.75
		table_3.plate2 = 7.82
		table_3.plate3 = 6.53
		table_3.plate4 = 19.23
		table_3.plate5 = 5.95

		# Instantiate fourth bill
		table_4 = RestaurantBill()
		# Assign class's attributes
		table_4.tableNumber = 'Table 4'
		table_4.plate1 = 2.52
		table_4.plate2 = 6.66
		table_4.plate3 = 10.35
		table_4.plate4 = 7.88
		table_4.plate5 = 4.81

		# Instantiate fifth bill
		table_5 = RestaurantBill()
		# Assign class's attributes
		table_5.tableNumber = 'Table 5'
		table_5.plate1 = 13.42
		table_5.plate2 = 12.73
		table_5.plate3 = 8.74
		table_5.plate4 = 9.99
		table_5.plate5 = 9.87

		# Array to print out links
		bills = [table_1,table_2,table_3,table_4,table_5]

		

		# Shows the header html
		self.response.write(detail.header())
		# Shows the form html
		self.response.write(detail.form())
		# If statment to populate links
		if self.request.GET:
			bill = (int(self.request.GET['bill']))-1
			self.response.write(self.html(bills[bill]))
		# Shows the footer html
		self.response.write(detail.footer())



	# Function to total each tables bill as well as show the total and each persons meal cost
	def html(self,obj):
		# Varaible equal to the total of the tables meals
		total = obj.plate1 + obj.plate2 + obj.plate3 + obj.plate4 + obj.plate5
		# Variable to display the details of each tables bill
		result = '''
		<div class = 'container'>
			<div>
				<h1>{obj.tableNumber}</h1>
				<ul>
					<li>First Order: ${obj.plate1}</li>
					<li>Second Order: ${obj.plate2}</li>
					<li>Third Order: ${obj.plate3}</li>
					<li>Fourth Order: ${obj.plate4}</li>
					<li>Fifth Order: ${obj.plate5}</li>
					<li id='total'>Bill Total: ${total}</li>
				</ul>
			</div>
		</div>'''
		# Format method for big strings
		result = result.format(**locals())
		# Returning result so it can be populated on screen
		return result

# Creating a class and passing it object for the inheratince
class RestaurantBill(object):
	# Init function
	def __init__(self):
		# Seven attributes of the class
		self.tableNumber = ''
		self.plate1 = 0
		self.plate2 = 0
		self.plate3 = 0
		self.plate4 = 0
		self.plate5 = 0
		self.__total = 0

	# Property for __total
	@property
	def total(self):
		return self.__total

	# Setter for __total
	@total.setter
	def total(self, t):
		self.__total = t
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
