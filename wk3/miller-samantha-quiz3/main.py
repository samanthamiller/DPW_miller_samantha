import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		pass

class Shoes(object):
	def __init__(self):
		self.brand = ''
		self.color = ''
		self._size = ''

	@property
	def shoeBrand(self):
		return self._size

	def printSize(self):
		print self.size

	def printInfo(self):
		print self.brand + self.color


class Heels(Shoes):
	def __init__(self):
		super(Wedges,self).__init__()
		self.heel_size = ''
		self.type = ''
	@property
	def heel_height(self):
		return self.heel_size

class Sneakers(Shoes):
	def __init__(self):
		super(Sneakers, self).__init__()
		self.athletic_type = ''
		self.grip_level = ''

	@property
	def sport(self):
		return self.athletic_type


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
