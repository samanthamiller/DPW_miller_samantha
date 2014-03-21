import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		pass

class Shoes(object):
	def __init__(self):
		self.brand = ''
		self.color = ''
		self._size = ''

	def printColor(self):
		print self.color

	def printSize(self):
		print self.size

	def printBrand(self):
		print self.brand

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


app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
