import webapp2
# We need this for requesting info from API
import urllib2
# Library for working with xml in python
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
	''' This is the main controler for my weather application '''
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
			wm.send() # Tells model to send the info and get the data
			wv = WeatherView() # Creates view
			print 'View got data from model'
			wv.do = wm.do # Pass data from model to view
			self.response.write(wv.content)



class WeatherModel(object):
	'''  This model handles fetching, parsing and sorting data from the weather api '''
	def __init__(self, zip):
		self.__url = 'http://xml.weather.yahoo.com/forecastrss?p='
		self.__request = urllib2.Request(self.__url + zip)
		self.__opener = urllib2.build_opener()

	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort() # Call the method that sorts the xml doc

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result)
		self.__dos = []

		list = self.__xmldoc.getElementsByTagName('yweather:forecast')
		for l in list:
			do = WeatherData()
			do.code = l.attributes['code'].value
			do.day = l.attributes['day'].value
			do.high = l.attributes['high'].value
			do.low = l.attributes['low'].value
			do.condition = l.attributes['text'].value
			self.__dos.append(do)

	@property
	def dos(self):
		return self.__dos # Returns data object with all our delicious info


class WeatherData(object):
	'''  This data object holds the dta fetched by the model and shown by the view '''
	def __init__(self):
		# Data objects are public
		self.title = ''
		self.day = ''
		self.high = ''
		self.low = ''
		self.code = ''
		self.condition = ''

class WeatherView(object):
	''' This class handles how the data is shown to the user '''
	def __init__(self):
		self.__do = WeatherData()
		print 'Weather View function ran'

	def update(self): # Update the apperance of the view
		self.__content = '<h3>' + self.__do.title + '</h3>'
		self.__content += self.__do.day + ' -'
		self.__content += ' High: ' + self.__do.high
		self.__content += ' Low: ' + self.__do.low
		self.__content += ' Condition: ' + self.__do.condition
		self.__content += '<br/>'
		print self.__content


	@property
	def do(self):
		return self.__do 

	@do.setter
	def do(self,new_do):
		self.__do = new_do
		self.update()
		print self.__do.title

	@property
	def content(self):
		return self.__content

class Page(object):
	'''  This class handles basic html components of the web page '''
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
	'''  This handles form components and html components for web page '''
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
