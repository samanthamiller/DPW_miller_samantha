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

			wm = WeatherModel(zip) # Sends zip to model
			wm.send()



class WeatherModel(object):
	def __init__(self, zip):
		self.__url = 'http://xml.weather.yahoo.com/forecastrss?p='
		self.__request = urllib2.Request(self.__url + zip)
		self.__opener = urllib2.build_opener()

	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort() # Call the method that sorts the xml doc

	def sort(self):
		print 'Sort function ran'
		self.__xmldoc = minidom.parse(self.__result)
		self.__do = WeatherData()
		self.__do.title = self.__xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue
		list = self.__xmldoc.getElementsByTagName('yweather:forecast')
		for l in list:
			print l.attributes['day'].value
			self.__do.code = l.attributes['code'].value
			self.__do.day = l.attributes['day'].value
			self.__do.high = l.attributes['high'].value
			self.__do.low = l.attributes['low'].value
			self.__do.condition = l.attributes['text'].value


class WeatherData(object):
	def __init__(self):
		# Data objects are public
		self.title = ''
		self.day = ''
		self.high = ''
		self.low = ''
		self.code = ''
		self.condition = ''

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
