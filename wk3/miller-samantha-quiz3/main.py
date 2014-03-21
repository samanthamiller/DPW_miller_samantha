import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# Instantiate shoes class
		shoes = Shoes()

		heels = Heels()
		heels.brand = 'Derion '
		heels.color = 'Brown '
		heels.size = '7 '
		heels.heel_size = '6 '
		heels.type = 'Boot '
		heels.printInfo()

class Shoes(object):
	def __init__(self):
		self.brand = ''
		self.color = ''
		self._size = ''

	@property
	def shoeBrand(self):
		return self._size

	@property
	def shoeColor(self):
		return self.color

	def printSize(self):
		print self.size

	def printInfo(self):
		print self.brand + self.color


class Heels(Shoes):
	def __init__(self):
		super(Heels,self).__init__()
		self.heel_size = ''
		self.type = ''
	@property
	def heel_height(self):
		return self.heel_size

	def printInfo(self):
		print self.brand + self.color + self.heel_size + self.type

class Sneakers(Shoes):
	def __init__(self):
		super(Sneakers, self).__init__()
		self.athletic_type = ''
		self.grip_level = ''

	@property
	def sport(self):
		return self.athletic_type

	def printInfo(self):
		print self.brand + self.color + self.athletic_type + self.grip_level


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
