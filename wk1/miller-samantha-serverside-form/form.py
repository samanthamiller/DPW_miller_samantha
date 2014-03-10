class Form():
	def __init__(self, main_self):
		pass
		self.head = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Address Book</title>
			</head> 
		<body>'''
		self.form = ''' 
		<form method='GET' action='' 
		<input type='text' name='first_name' placeholder='First Name'/>
		<input type='text' name='last_name' placeholder='Last Name'/>
		<input type='text' name='phone_number' placeholder='Phone Number'/>
		<select>
			<option value="Home">Home</option>
	  		<option value="Cell">Cell</option>
	  		<option value="Work">Work</option>
		</select>
		<input type='checkbox' name='relationship' value='Friend'/>
		<input type='checkbox' name='relationship value='Family'/>
		<input type='checkbox' name='relationship value='Co-worker'/>
		'''

