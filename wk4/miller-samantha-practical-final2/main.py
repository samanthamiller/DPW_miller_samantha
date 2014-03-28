import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
	def get(self):
		page = MainPage()
		self.response.write(page.return_main_page())

class TopModel(object):
	def __init__(self):
		self.__url = 'http://rebeccacarroll.com/api/music/music.xml'
		self.__request = urllib2.Requwst(self.__url)
		self.__opener = urllib2.build_opener()
		self.send()

	def send(self):
		self.__result = self.__opener.open(self.__request)
		self.sort()

	def sort(self):
		self.__xmldoc = minidom.parse(self.__result)
		self.__music_data = TopData()

		music = self.__xmldoc.getElementsByTagName('track')

		for i in music:
			music_dict = dict()

			title = song.getElementsByTagName('title')[0].firstChild.nodeValue
			artist = song.getElementsByTagName('artist')[0].firstChild.nodeValue
			music_dict = [title, artist]

			self.__data.music.append(music_dict)
	@property
	def music_data(self):
		return self.__music_data

class TopData(object):
	def __init__(self):
		self.music = []

class TopView(object):
	def __init__(self, music_data):
		self.__content = ' '
		for i in music_data.music:
			self.__content += "<button href='?song=0'>"+music[0]+"</button>"
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
