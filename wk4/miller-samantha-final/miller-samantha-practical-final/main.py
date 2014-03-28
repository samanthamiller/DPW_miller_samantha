import webapp2
# Needed for getting json
import urllib2
# Needed for parsing json
import json

class MainHandler(webapp2.RequestHandler):
	''' This is the mainhandler which controls what information is viewed '''
	def get(self):
		# Instantiating the class MainPage()
		page = MainPage()
		# Populating the basic html set up by calling a function that lives in the MainPage class
		self.response.write(page.return_main_page())

		if self.request.GET:
		 	print 'If statment is being ran'
			tm = TopModel()
			tm.send()
			tv = TopView()
			tv.do = tm.do
			self.response.write(tv.content)




class TopModel(object):
	''' This class requests, recives, validates and sorts the json data '''
	def __init__(self):
		# Which api to pull from
		self.__url = 'http://rebeccacarroll.com/api/music/music.json'
		# To assemble a request
		self.__request = urllib2.Request(self.__url)
		# Create object to get the url
		self.__opener = urllib2.build_opener()

	# Function to use the url and get a result and request information from the api
	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort()

	# Function to parse and sort information
	def sort(self):
		# Parsing the json results
		self.__json_data = json.load(self.__result)
		# Empty array for the data objects to be appended to
		self.__populate = []
		# For loop to pull neccesary information from api
		for i in self.__json_data['songs']:
			do = TopData()
			do.title = i['title']
			do.artist = i['artist']
			do.length = i['length']
			do.year = i['year']
			do.label = i['label']
			do.cover = i['cover']
			# Appending every tracks infromation to the empty __populate array
			self.__populate.append(do)

	# Returning populate so that it can be used
	@property
	def populate(self):
		return self.__populate

# Storing returned data from api
class TopData(object):
	''' This class stores data returned form the api '''
	def __init__(self):
		# Public
		self.title = ''
		self.artist = ''
		self.length = ''
		self.year = ''
		self.label = ''
		self.cover = ''

class TopView(object):
	''' This controles the view '''
	def __init__(self):
		# Setting populate equal to the stored information of TopData
		self.__populate = TopData()
	def update(self, new_p):
		# Variable to push content into
		self.__content = ''
		# Loop to populate each top's info
		for i in new_p:
			self.__populate = i
			self.__content += '<p>'+i.title+'</p>'
			self.__content += '<p>'+i.artist+'</p>'
			self.__content += '<p>'+i.length+'</p>'
			self.__content += '<p>'+i.year+'</p>'
			self.__content += '<p>'+i.label+'</p>'
			self.__content += '<p>'+i.cover+'</p>'

	# Returing information through getter
	@property
	def populate(self):
		return self.__populate

	# Using setter to set new values
	@populate.setter
	def populate(self, new_populate):
		self.update(new_populate)

	# Returning information through getter
	@property
	def content(self):
		return self.__content


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
