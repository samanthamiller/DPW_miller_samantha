import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

class Shoes(object):
	def __init__(self):
		pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
