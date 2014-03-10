class Form():
	def __init__(self, main_self):
		pass
		# Creating a head variable to contain the html head code
		self.head = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Address Book</title>
			</head> 
		<body>'''
		# Creating a form variable to contain the html form code
		self.form = ''' 
		<form method='GET' action=''> 
			<input type='text' name='first_name' placeholder='First Name'/>
			<input type='text' name='last_name' placeholder='Last Name'/>
			<input type='text' name='phone_number' placeholder='Phone Number'/>
			<select>
				<option value='Home'>Home</option>
		  		<option value='Cell' selected='selected'>Cell</option>
		  		<option value='Work'>Work</option>
			</select>
			<p>Friend</p><input type='checkbox' name='relationship' value='Friend'/>
			<p>Family</p><input type='checkbox' name='relationship value='Family'/>
			<p>Co-worker</p><input type='checkbox' name='relationship value='Co-worker'/>
			<input type='submit' value ='Enter'/>
		</form>	
		'''
		self.footer = '''</body></html>'''

	def print_contents(self, i=''):
		if i=='':
			return self.head + self.form + self.footer
		else:
			return self.head + i + self.footer

