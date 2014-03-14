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

class Lion(Animal):
	def __init__(self):
		super(Lion,self).__init__()
		self.phylum = 'Chordata'
		self.animal_class = 'Mammalia'
		self.order = 'Carnivora'
		self.family = 'Felidea'
		self.genus = 'Panthera'
		self.image = ''
		self.lifespan = '15'
		self.habitat = 'Sub-Saharan Africa except in desert and rainforest habitats.'
		self.geolocation = ''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
