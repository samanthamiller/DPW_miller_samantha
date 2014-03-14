import webapp2
from details import Details

class MainHandler(webapp2.RequestHandler):
    def get(self):
        details = Details()
        self.response.write(details.header)
        self.response.write(details.body)
        self.response.write(details.footer)

class Animal(object):
	def __init__(self):
		self.phylum = ''
		self.animal_class = ''
		self.order = ''
		self.family = ''
		self.genus = ''
		self.image = ''
		self.lifespan = ''
		self.habitat = ''
		self.geolocation = ''
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
