import webapp2
# Needed for getting json
import urllib2
# Needed for parsing json
import json

class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = MainPage()
		self.response.write(page.return_main_page())


class MainPage(object):
	''' This class is going to handle basic html page elements '''
	def __init__(self):
		# Setting up html's head information
		self._head = ''' <!DOCTYPE HTML> 
		<html>
			<head>
				<title>Final Practical</title>
			</head>
			<body>
		'''
		# Seting variable equal to an empty sting because that is where information will be populating later
		self._body = ''' <h1> Top ten songs </h1>'''
		# Closing html elements
		self._footer = ''' 
			</body>
		</html>'''

	# Function to return the attributes _head, _body and _footer which create the thml
	def return_main_page(self):
		return self._head + self._body + self._footer
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
