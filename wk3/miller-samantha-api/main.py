import webapp2
# Need this for requesting info from api
import urllib2
# Import json
import json

class MainHandler(webapp2.RequestHandler):
	''' This is the main controller for my recipe search application '''
	def get(self):
		# Instanciate FormPage
		page = FormPage()
		# Put input feilds into html and populate
		self.response.write(page.print_out())

		# If there is information on the url
		if self.request.GET:
			# Get the information in the url
			ingredient = self.request.GET['ingredient']
			rm = RecipeModel(ingredient)
			rm.send()
			rv = RecipeView()
			rv.populate = rm.populate
			self.response.write(rv.content)
			


class RecipeModel(object):
	def __init__(self, ingredient):
		self.__url = 'http://www.recipepuppy.com/api/?q='
		self.__request = urllib2.Request(self.__url + ingredient)
		self.__opener = urllib2.build_opener()

	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort()

	def sort(self):
		self.__json_data = json.load(self.__result)
		self.__populate = []

		for i in self.__json_data['results']:
			self.__populate = RecipeData()
			self.__populate.title =  i['title']
			self.__populate.ingredients =  i['ingredients'] 
			self.__populate.href =  i['href'] 

	@property
	def populate(self):
		return self.__populate

class RecipeData(object):
	def __init__(self):
		self.title = ''
		self.ingredients = ''
		self.href = ''

class RecipeView(object):
	def __init__(self):
		self.__populate = RecipeData()

	def upadate(self):
		self.__content = "<div id='results' class='container sixteen columns'>"
		self.__content += '<h3>' + self.__populate.title + '</h3>'
		self.__content +=  '<p>Ingredients: ' + self.__populate.ingredients + '</p>'
		self.__content += "<a href=" + self.__populate.href + "> View Recipe </a>"
		self.__content += '</div>'
		self.__content += '<br/>'

	@property
	def populate(self):
		return self.__populate

	@populate.setter
	def populate(self, new_populate):
		self.__populate = new_populate
		self.upadate()

	@property
	def content(self):
		return self.__content


class Page(object):
	def __init__(self):
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
		'''
		self._body = ''' '''
		self._footer = ''' 
			</body>
		</html>
		'''
		@property 
		def body(self):
			pass

		@body.setter
		def body(self, b):
			self.body = b

	def print_out(self):
		return self._head + self._body + self._footer

class FormPage(Page):
	def __init__(self):
	# Run the instantiating function for the Super Class
	# Pass in the name of the subclass and self
		super(FormPage, self).__init__()
		self.__form_open = "<div id='searchForm' class='container sixteen columns'> <div class='fourteen columns'> <form method='GET'>"
		self.__input = ''' <input type='text' placeholder='Ingredient' name='ingredient'>
		<input type='submit' value='Search'>  '''
		self.__form_close = '</form></div></div>'

	def print_out(self):
		return self._head + self.__form_open + self.__input + self.__form_close + self._footer



app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
