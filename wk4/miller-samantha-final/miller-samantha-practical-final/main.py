import webapp2
# Neet to read xml data
import urllib2
# Need to parse xml
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
	''' This class controles how the model and view interact '''
	def get(self):
		# Instantiate the class MainPage
		page = MainPage()
		# Put html elements on the page
		self.response.write(page.return_main_page())
		# Instantiate Model 
		tm = TopModel()
		# Instantiate View and pass it data object
		tv = TopView(tm.music_data)
		# Print content 
		self.response.write(tv.content)

class TopModel(object):
	''' This class handels requesting, recieving, validating and sorting data '''
	def __init__(self):
		# Gets the api
		self.__url = 'http://rebeccacarroll.com/api/music/music.xml'
		# Request's informatino from api
		self.__request = urllib2.Request(self.__url)
		self.__opener = urllib2.build_opener()
		# Call send function
		self.send_data()

	# Function to send information
	def send_data(self):
		self.__result = self.__opener.open(self.__request)
		# Call sort function
		self.sort()

	# Function that parses xml data and collects information
	def sort(self):
		# Parsing xml data
		self.__xmldoc = minidom.parse(self.__result)
		# Setting music data equal to the class TopData
		self.__music_data = TopData()

		# Getting the track array
		music = self.__xmldoc.getElementsByTagName('track')

		# Looping thorugh music which is the track array
		for i in music:
			# Create a dictionary 
			music_dict = dict()
			# Get all of this information from the api
			title = i.getElementsByTagName('title')[0].firstChild.nodeValue
			artist = i.getElementsByTagName('artist')[0].firstChild.nodeValue
			length = i.getElementsByTagName('length')[0].firstChild.nodeValue
			year = i.getElementsByTagName('year')[0].firstChild.nodeValue
			label = i.getElementsByTagName('label')[0].firstChild.nodeValue
			cover = i.getElementsByTagName('cover')[0].firstChild.nodeValue
			# Adding elements found to dictionary 
			music_dict = [title, artist, length, year,label,cover]
			# Append the dictionary objects to musoc data
			self.__music_data.music.append(music_dict)

	# Return music data
	@property
	def music_data(self):
		return self.__music_data


class TopData(object):
	''' This class holds an array of the tracks data'''
	def __init__(self):
		self.music = []

class TopView(object):
	''' The view of what will be shown in the html '''
	def __init__(self, music_data):
		# Open a variable for informatino to be pushed into
		self.__content = ' '
		# Loop through music data
		for i in music_data.music:
			self.__content += "<a href='?music='>"+i[0]+"</a>"
			self.__content += "<br/>"
			self.__content += '<p> Artist: ' +i[1]+ '</p>'
			self.__content += '<p> Song Length: ' +i[2]+ '</p>'
			self.__content += '<p> Year Released: ' +i[3]+ '</p>'
			self.__content += '<p> Record Label: ' +i[4]+ '</p>'
			self.__content += "<img src='"+i[5]+ "'>"

			print i[0]

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
