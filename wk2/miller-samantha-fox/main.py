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
		# Assign information to attributes passed down from Lion's superclass Animal
		lion.phylum = 'Chordata'
		lion.animal_class = 'Mammalia'
		lion.order = 'Carnivora'
		lion.family = 'Felidea'
		lion.genus = 'Panthera'
		lion.image = 'https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg'
		lion.lifespan = '15'
		lion.habitat = 'Tropical'
		lion.geolocation = 'Sub-Saharan Africa'
		lion.sound = 'Rawr'

		# Instantiate the Kangaroo subclass
		kangaroo = Kangaroo()
		# Assign information to attributes passed down from Kangaroo's superclass Animal
		kangaroo.phylum = 'Chordata'
		kangaroo.animal_class = 'Mammalia'
		kangaroo.order = 'Diprotodontia'
		kangaroo.family = 'Macropodidae'
		kangaroo.genus = 'Macropus'
		kangaroo.image = 'https://upload.wikimedia.org/wikipedia/commons/5/5d/RedRoo.JPG'
		kangaroo.lifespan = '15'
		kangaroo.habitat = 'Forest'
		kangaroo.geolocation = 'Southern Australia'
		kangaroo.sound = 'Tut-tut'

		# Instantiate the PatasMonkey subclass
		monkey = PatasMonkey()
		monkey.phylum = 'Chordata'
		monkey.animal_class = 'Mammalia'
		monkey.order = 'Primates'
		monkey.family = 'Cercopithecidae'
		monkey.genus = 'Erythrocebus'
		monkey.image = 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Patas_Monkey_Jr.jpg'
		monkey.lifespan = '15'
		monkey.habitat = 'Grassland'
		monkey.geolocation = 'Ethiopia'
		monkey.sound = 'Ohh-ee'

		# Array to populate animal information
		animals = [lion, kangaroo, monkey]
		self.response.write(details.header + details.body + details.footer)
		if self.request.GET:
			animal = (int(self.request.GET['animal']))-1
			self.response.write(self.html(animals[animal]))

	def html(self,obj):
		result = '''
		<ul>
			<li>Phylum: {obj.phylum}</li>
			<li>Class: {obj.animal_class}</li>
			<li>Order: {obj.order}</li>
			<li>Family: {obj.family}</li>
			<li>Genus: {obj.genus}</li>
			<li>Image: <img src="{obj.image}" height="150" width="200"/></li>
			<li>Lifespan: {obj.lifespan}</li>
			<li>Habitat: {obj.habitat}</li>
			<li>Geolocation: {obj.geolocation}</li>
		</ul>
		'''
		# Format method for big strings
		result = result.format(**locals())
		# Returning result to be populated on screen
		return result

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

class PatasMonkey(Animal):
	def __init__(self):
		super(PatasMonkey,self).__init__()

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
