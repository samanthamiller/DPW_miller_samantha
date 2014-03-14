import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		fp = FormPage()
		fp.inputs = {'first_name':'text', 'last_name':'text', 'Submit':'submit'}
		fp.create_inputs()
		self.response.write(fp.print_out())

		'''p = Page()
		p.body = 'Hello World'
		self.response.write(p.print_out())'''

class Page(object):
	def __init__(self):
		self._head = '''  <!DOCTYPE HTML>
		<html>
			<head>
				<title>Polymorphism</title>
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
