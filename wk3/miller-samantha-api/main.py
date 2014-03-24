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
		# Create form input feild and submit button
		page.inputs = {'ingredient':'text', 'Search': 'submit'}
		# Run classes create_inputs method
		page.create_inputs()
		# Put input feilds into html and populate
		self.response.write(page.print_out())

		# If there is information on the url
		if self.request.GET:
			# Get the information in the url
			ingredient = self.request.GET['ingredient']
			url = 'http://www.recipepuppy.com/api/?q='
			# Assemble request
			request = urllib2.Request(url + ingredient)
			# Use urllib2 to create an object to get the url
			opener = urllib2.build_opener()
			# Use url to populate a result - request information from the api
			result = opener.open(request)

			# Parse the json result
			json_data = json.load(result)
			content = '<br/>'

			for i in json_data['results']:
				content += "<div class='container sixteen columns'"
				content += '<br/>'
				content += "<img src=" + i['thumbnail'] + "/>"
				content += '<br/>'
				content += '<p>' + i['title'] + '</p>'
				content += '<br/>'
				content +=  '<p>Ingredients: ' + i['ingredients'] + '</p>'
				content += '<br/>'
				content += "<a href=" + i['href'] + "> View Recipe </a>"
				content += '</div>'
			self.response.write(content)



class Page(object):
	def __init__(self):
		self._head = '''  <!DOCTYPE HTML>
		<html>
			<head>
				<title>Recipe finder</title>
				<link rel='stylesheet' type='text/css' href='css/base.css'/>
				<link rel='stylesheet' type='text/css' href='css/layout.css'/>
				<link rel='stylesheet' type='text/css' href='css/skeleton.css'/>
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
		self.__form_open = "<div class='container sixteen columns'> <form method='GET'>"
		self.__form_close = '</form></div>'
		self.__inputs = dict()
		self.__input_string = ''

	def create_inputs(self):
		for key, value in self.__inputs.iteritems():
			self.__input_string += '<input type="' + value+ '"name="' +key+'"/>'
	def print_out(self):
		return self._head + self.__form_open + self.__input_string + self.__form_close + self._footer

	@property
	def inputs(self):
		pass

	@inputs.setter
	def inputs(self, dict):
		self.__inputs = dict

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
