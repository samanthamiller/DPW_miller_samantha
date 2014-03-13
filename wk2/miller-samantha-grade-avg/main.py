# Samantha Miller
# March 11, 2014
# Grade Average sike 

import webapp2
from detail import Detail
class MainHandler(webapp2.RequestHandler):
	def get(self):

		detail = Detail()

		self.table_1 = RestaurantBill()
		self.table_1.tableNumber = 'Table 1'
		self.table_1.plate1 = 7.50
		self.table_1.plate2 = 3.67
		self.table_1.plate3 = 6.53
		self.table_1.plate4 = 8.96
		self.table_1.plate5 = 6.78
		self.table_1.calc_total()
		print self.table_1.total

		self.table_2 = RestaurantBill()
		self.table_2.tableNumber = 'Table 2'
		self.table_2.plate1 = 8.95
		self.table_2.plate2 = 5.83
		self.table_2.plate3 = 3.99
		self.table_2.plate4 = 12.50
		self.table_2.plate5 = 14.78
		self.table_2.calc_total()
		print self.table_2.total

		self.table_3 = RestaurantBill()
		self.table_3.tableNumber = 'Table 3'
		self.table_3.plate1 = 3.75
		self.table_3.plate2 = 7.80
		self.table_3.plate3 = 6.53
		self.table_3.plate4 = 19.23
		self.table_3.plate5 = 5.95
		self.table_3.calc_total()
		print self.table_3.total

		self.table_4 = RestaurantBill()
		self.table_4.tableNumber = 'Table 4'
		self.table_4.plate1 = 2.50
		self.table_4.plate2 = 6.66
		self.table_4.plate3 = 10.35
		self.table_4.plate4 = 7.88
		self.table_4.plate5 = 4.81
		self.table_4.calc_total()
		print self.table_4.total

		self.table_5 = RestaurantBill()
		self.table_5.tableNumber = 'Table 5'
		self.table_5.plate1 = 13.40
		self.table_5.plate2 = 12.70
		self.table_5.plate3 = 8.74
		self.table_5.plate4 = 9.99
		self.table_5.plate5 = 9.87
		self.table_5.calc_total()
		print self.table_5.total

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

	def calc_total(self):
		total = self.plate1 + self.plate2 + self.plate3 + self.plate4 + self.plate5
		self.__total = total

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
