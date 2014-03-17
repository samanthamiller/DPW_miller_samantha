class Details(object):
	def __init__(self):
		self.header = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Animal Info</title>
			</head>
			<body>
		'''
		self.body = ''' 
		<form method='GET' name='animals' id='links'>
			<a href='/?animal=1' name = 'animal' class ='link' id='lion'>Lion</a>
			<a href='/?animal=2' name = 'animal' class ='link' id='kangaroo'>Kangaroo</a>
			<a href='/?animal=3' name = 'animal' class ='link' id='monkey'>Patas Monkey</a>
		</form>
		'''
		self.footer = ''' 
		</body>
		</html>'''

	def header(self):
		return self.header
	def body(self):
		return self.body
	def footer(self):
		return self.footer