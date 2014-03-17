# Samantha Miller
# March 17, 2014
# What does the fox say

import webapp2
from details import Details

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	# Instantiate the details class, contains the html.
        details = Details()
        # Instantiate the Lion subclass
        lion = Lion()
        lion.phylum = 'Chordata'
        lion.animal_class = 'Mammalia'
        lion.order = 'Carnivora'
        lion.family = 'Felidea'
        lion.genus = 'Panthera'
        lion.image = 'http://www.jogjis.com/stock/animal-mad-female-lion-growling-mad-hd-wallpaper.jpg'
        lion.lifespan = '15'
        lion.habitat = 'Tropical'
        lion.geolocation = 'Sub-Saharan Africa'
        # Instantiate the Kangaroo subclass
        kangaroo = Kangaroo()
        # Instantiate the PatasMonkey subclass
        monkey = PatasMonkey()
        self.response.write(details.header + details.body + details.footer)

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
		self.__sound = ''

		@property
		def sound(self):
			return self.__sound

		@sound.setter
		def sound(self, specific_sound):
			self.__sound = specific_sound

class Lion(Animal):
	def __init__(self):
		super(Lion,self).__init__()

class Kangaroo(Animal):
	def __init__(self):
		super(Kangaroo,self).__init__()
		self.phylum = 'Chordata'
		self.animal_class = 'Mammalia'
		self.order = 'Diprotodontia'
		self.family = 'Macropodidae'
		self.genus = 'Macropus'
		self.image = 'http://animaldiversity.ummz.umich.edu/accounts/Macropus_fuliginosus/pictures/collections/contributors/lynda_staker/Macropus_fuliginosus2/'
		self.lifespan = '15'
		self.habitat = 'Forest'
		self.geolocation = 'Southern Australia'

class PatasMonkey(Animal):
	def __init__(self):
		super(PatasMonkey,self).__init__()
		self.phylum = 'Chordata'
		self.animal_class = 'Mammalia'
		self.order = 'Primates'
		self.family = 'Cercopithecidae'
		self.genus = 'Erythrocebus'
		self.image = 'http://animaldiversity.ummz.umich.edu/accounts/Erythrocebus_patas/pictures/collections/contributors/corel_cd/patas/'
		self.lifespan = '15'
		self.habitat = 'Grassland'
		self.geolocation = 'Ethiopia'

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
