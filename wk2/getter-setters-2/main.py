import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
	def get(self):
    	# Triggers __init__ function in Page() class
		self.page = Page()
		self.page.title = 'Contact Us'
		self.response.write(self.page.all)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

# Data Objects
# Classes with no function
# No methods in it 

