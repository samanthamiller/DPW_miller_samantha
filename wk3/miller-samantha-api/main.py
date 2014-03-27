import webapp2
# Need this for requesting info from api
import urllib2
# Import json
import json

class MainHandler(webapp2.RequestHandler):
	''' This is the main controller for my recipe search application '''
	def get(self):
		# Instanciate of FormPage
		page = FormPage()
		# Put input feilds into html and populate
		self.response.write(page.print_out())

		# If there is information on the url
		if self.request.GET:
			# Get the information in the url
			ingredient = self.request.GET['ingredient']
			# Sends ingredient into model
			rm = RecipeModel(ingredient)
			# Tells model to send into and get the data
			rm.send()
			# Instantiates view
			rv = RecipeView()
			# Passes data collected from model to view
			rv.populate = rm.populate
			# Populates search results to the screen
			self.response.write(rv.content)
			


class RecipeModel(object):
	'''  This model handles fetching, parsing and sorting data from the recipe api '''
	def __init__(self, ingredient):
		# url location of the api i'm pulling from
		self.__url = 'http://www.recipepuppy.com/api/?q='
		# Assembles request
		self.__request = urllib2.Request(self.__url + ingredient)
		# Use urllib2 to create a object to get the url
		self.__opener = urllib2.build_opener()

	def send(self):
		# Use url to get a result - request information from the api
		self.__result = self.__opener.open(self.__request)
		# Call sort function 
		self.sort()

	def sort(self):
		# Parse the json result data
		self.__json_data = json.load(self.__result)
		# Empty array to push recipies into
		self.__populate = []

		# Looping through the json data results
		for i in self.__json_data['results']:
			# Instantiate RecipieData class 
			do = RecipeData()
			# Recipies title is equal to the information in the xml title variable
			do.title =  i['title']
			# Recipies ingredients is equal to the information in the xml ingredients variable
			do.ingredients =  i['ingredients'] 
			# Recipies href is equal to the information in the xml href variable
			do.href =  i['href']
			# Append do (All the recipie information) to the empty array __populate
			self.__populate.append(do)

	@property
	def populate(self):
		# Returns the data object __populate which now contains all the xml data we pulled
		return self.__populate

class RecipeData(object):
	'''  This data object holds the dta fetched by the model and shown by the view '''
	def __init__(self):
		# Data objects are public
		self.title = ''
		self.ingredients = ''
		self.href = ''

class RecipeView(object):
	''' This class handles how the data is shown to the user '''
	def __init__(self):
		# Sets populate equal to the RecipeData class
		self.__populate = RecipeData()

	# Function to update each recipies content 
	def update(self, np):
		# Set variable content equal to empty string
		self.__content = ''
		# Loop through each recipe recieved
		for i in np:
			# Populate is equal to array value
			self.__populate = i
			# Add a div around each recipe's data
			self.__content += "<div class='container sixteen columns results'>"
			# Make the titles of the recipe's h4's
			self.__content += '<h4>' + i.title + '</h4>'
			# Make the ingredients of the recipe's paragraps
			self.__content +=  '<p>Ingredients: ' + i.ingredients + '</p>'
			# Make the recipe link a link
			self.__content += "<a href=" + i.href + "> View Recipe </a>"
			# Close containing div 
			self.__content += '</div>'

	# Property returning populate
	@property
	def populate(self):
		return self.__populate


	@populate.setter
	def populate(self, new_populate):
		# Calling update function and passing it new_populate
		self.update(new_populate)

	@property
	def content(self):
		# Return the content
		return self.__content


class Page(object):
	'''  This class handles basic html components of the web page '''
	def __init__(self):
		# Creates basic html head elements
		self._head = '''  <!DOCTYPE HTML>
		<html>
			<head>
				<title>Recipe finder</title>
				<link rel='stylesheet' type='text/css' href='css/base.css'/>
				<link rel='stylesheet' type='text/css' href='css/layout.css'/>
				<link rel='stylesheet' type='text/css' href='css/skeleton.css'/>
				<link rel='stylesheet' type='text/css' href='css/style.css'/>
			</head>
			<body>
				<div id = 'header' class ='container'>
					<h1>Pantry Raid</h1>
				</div>
		'''
		# Empty body container to push content into later
		self._body = ''' '''
		# Closes html document
		self._footer = ''' 
			</body>
		</html>
		'''
	# Function to return each of the attributes created
	def print_out(self):
		return self._head + self._body + self._footer

# Sub class of the Page class, inhearites pages methods and attributes
class FormPage(Page):
	def __init__(self):
		# Run the instantiating function for the Super Class
		# Pass in the name of the subclass and self
		super(FormPage, self).__init__()
		# Wrapping divs around he form elements
		self.__form_open = "<div id='searchForm' class='container sixteen columns'> <div class='fourteen columns'> <form method='GET'>"
		# Creating text and submit button html elements
		self.__input = ''' <input type='text' placeholder='Ingredient' name='ingredient'>
		<input type='submit' value='Search'>  '''
		# Closing the form and divs 
		self.__form_close = '</form></div></div>'

	# Repurposing superclass's method by adding in this classes attributes __form_open, __input and __form_close
	def print_out(self):
		return self._head + self.__form_open + self.__input + self.__form_close + self._footer



app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
