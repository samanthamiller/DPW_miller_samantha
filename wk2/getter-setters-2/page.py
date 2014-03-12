class Page(object):
	def __init__(self):
		self.head = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>{self.title}</title>
			</head>
			<body>		
		'''
		self.body = ''' 
		<a href='?fruit'=strawberry'>Strawberry</a>
		<a href='?fruit=pear'>Pear</a>
		<a href='?fruit=banana'>Banana</a>
		'''
		self.close = '''
		</body>
		</html>
		'''
		# self.all = self.head + self.body + self.close
		self.update_page()
		self.__title = 'Welcome!'
	def update_page(self):
		self.all = self.head + self.body + self.close
	
	# Property for __title 	
	@property
	def title(self):
		return self.__title

	@title.setter
	def title(self, title):
		self.__title = title
		# Reformat the self.all string so that it incorporates our title
		self.all = self.all.format(**locals())



		