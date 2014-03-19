import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = FormPage()
        page.inputs = {'alcoholType':'text', 'Submit':'submit'}
        page.create_inputs()
        self.response.write(page.print_out())

        if self.request.GET:
            alcoholType = self.request.GET['alcoholType']
            url = 'http://www.barnivore.com/search.xml?keyword='

            request = urllib2.Request(url + alcoholType)
            opener = urllib2.build_opener()
            result = opener.open(request)
            xmldoc = minidom.parse(result)
            content = ''

            companies = xmldoc.getElementsByTagName('company')

            for company in companies:
                try:
                    address = company.getElementsByTagName('address')
                except: StandardError
                    address = "No Address on File"
                content += "<h3>" + company.getElementsByTagName('company-name')[0].firstChild.nodeValue + "</h3>"
                content += "<h4>" + address + "</h4>"
                content += "<br/>"
            self.response.write(content)

class Page(object):
    def __init__(self):
        self._head = '''  <!DOCTYPE HTML>
        <html>
            <head>
                <title>Vegan Alcohol Guide</title>
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
