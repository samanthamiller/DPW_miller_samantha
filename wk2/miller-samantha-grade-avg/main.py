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
		table_1.plate1 = 7.50
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
		table_2.plate4 = 12.50
		table_2.plate5 = 14.78

		# Instantiate third bill
		table_3 = RestaurantBill()
		# Assign class's attributes
		table_3.tableNumber = 'Table 3'
		table_3.plate1 = 3.75
		table_3.plate2 = 7.80
		table_3.plate3 = 6.53
		table_3.plate4 = 19.23
		table_3.plate5 = 5.95

		# Instantiate fourth bill
		table_4 = RestaurantBill()
		# Assign class's attributes
		table_4.tableNumber = 'Table 4'
		table_4.plate1 = 2.50
		table_4.plate2 = 6.66
		table_4.plate3 = 10.35
		table_4.plate4 = 7.88
		table_4.plate5 = 4.81

		# Instantiate fifth bill
		table_5 = RestaurantBill()
		# Assign class's attributes
		table_5.tableNumber = 'Table 5'
		table_5.plate1 = 13.40
		table_5.plate2 = 12.70
		table_5.plate3 = 8.74
		table_5.plate4 = 9.99
		table_5.plate5 = 9.87

		# Array to 
		bills = [table_1,table_2,table_3,table_4,table_5]

		self.response.write(detail.header())
		self.response.write(detail.form())
		if self.request.GET:
			bill = (int(self.request.GET['bill']))-1
			print bill
			self.response.write(self.html(bills[bill]))
		self.response.write(detail.footer())

	def html(self,obj):
		total = obj.plate1 + obj.plate2 + obj.plate3 + obj.plate4 + obj.plate5
		result = '''
		<div id="result">
			<h1>{obj.tableNumber}</h1>
			<ul>
				<li>{obj.plate1}</li>
				<li>{obj.plate2}</li>
				<li>{obj.plate3}</li>
				<li>{obj.plate4}</li>
				<li>{obj.plate5}</li>
				<li>{total}</li>
			</ul>
		</div>'''
		result = result.format(**locals())
		return result

class RestaurantBill(object):
	def __init__(self):
		self.tableNumber = ''
		self.plate1 = 0
		self.plate2 = 0
		self.plate3 = 0
		self.plate4 = 0
		self.plate5 = 0
		self.__total = 0

	@property
	def total(self):
		return self.__total

	@total.setter
	def total(self, t):
		self.__total = t


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
