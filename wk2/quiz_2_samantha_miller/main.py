class Cats(object):
	def __init__(self):
		self.__name = ''
		self.__breed = ''
		self.age = 0

		@property
		def age(self):
			return self.__age

		@age.setter
		def age(self, years):
			self.__age = years

	def print_info(n, b, a):
		cat_info = n + ' is a ' + a + ' year old ' + b + ' cat.'
		print cat_info

	def print_cat_name(a):
		name = a
		print name

class VetBill(object):
	def __init__(self):
		