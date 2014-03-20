import webapp2
# We need this for requesting info from API
import urllib2
# Library for working with xml in python
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = FormPage()
		page.inputs = {'zip':'text', 'Submit':'submit'}
		page.create_inputs()
		self.response.write(page.print_out())

		# If there is info in the url
		if self.request.GET:
			# Lets get that information in the url
			zip = self.request.GET['zip']
			url = 'http://xml.weather.yahoo.com/forecastrss?p='

			# Assemble request
			request = urllib2.Request(url + zip)

			# Use urllib2, to create an object to get the url
			opener = urllib2.build_opener()

			# Use url to get a result - request info from api
			result = opener.open(request)

			# Parse the result
			xmldoc = minidom.parse(result)
			self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)

			content = '<br/>'
			list = xmldoc.getElementsByTagName('yweather:forecast')
			for l in list:
				content += l.attributes['day'].value
				content += "    HIGH: " + l.attributes['high'].value
				content += "   	LOW: " + l.attributes['low'].value
				content += "   	CONDITION: " + l.attributes['text'].value
				# content += ' img src="http://l.yimg.com/a/i/us/we/52/' + l.attributes['code'].value + '.gif"/>'
				content += ' <img src="images/' + l.attributes['code'].value + '.png" width="50"/>'
				content += '<br/>'
			self.response.write(content)

class Page(object):
	def __init__(self):
		self._head = '''  <!DOCTYPE HTML>
		<html>
			<head>
				<title>Weather App - Yahoo API</title>
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
		self.__form_open = '<form method="GET">'
		self.__form_close = '</form>'
		self.__inputs = dict()
		self.__input_string = ''

		#{'first_name': 'text', 'last_name': 'text'}

	def create_inputs(self):
		for key, value in self.__inputs.iteritems():
			print key
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
