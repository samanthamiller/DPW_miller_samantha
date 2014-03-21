import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

class Shoes(object):
	def __init__(self):
		self.color = ''
		self._size = ''

	def printColor(self):
		print self.color

	def printSize(self):
		print self.size

class Wedges(Shoes):
	def __init__(self):
		super(Wedges,self).__init__()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
