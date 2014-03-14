class Details(object):
	def __init__(self):
		self.header = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Animal Info</title>
			</head>
			<body>
		'''
		self.body = ''' '''
		self.footer = ''' 
		</body>
		</html>'''

	def header(self):
		return self.header
	def body(self):
		return self.body
	def footer(self):
		return self.footer