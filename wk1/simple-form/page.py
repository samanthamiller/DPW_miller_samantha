class Page():

	# Methods - Methods are behaviors that store code
	# Attributes - Variables that store data
	# Constructor function
	def __init__(self):
		# Initilizing function - Constructor 
		pass
		# Traits
		self.__id = 74638493 # __ = Private
		self.author = 'Dean Koontz' # none = Public
		self._title = 'Odd Thomas' # _ = Protected
		self.head = """ <!DOCTYPE HTML>
		<html>
			<head>
			<title>Simple Form</title>
			<link rel='stylesheet' type='text/css' href='main.css'/>
				<title></title>
			</head>
		<body>"""
		self.body = "Hello World"
		self.form = '''
		<form method='GET' action=''>
			<input type='text' name='first_name'/>
			<input type='text' name='last_name'/>
			<input type='submit' value='Enter'/>
		</form>
		'''
		self.ender = """</body></html>"""

	def print_contents(self):
		return self.head + self.body + self.form + self.ender
		
class Button():
	def __init__(self):
		self.label = 'Contact Me'
		self.size = 100