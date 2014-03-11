class Form():
	def __init__(self, main_self):
		
		# Creating a head variable to contain the html head code
		self.head = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Phone Book</title>
				<link rel='stylesheet' type='text/css' href='css/main.css'/>
				<link rel='stylesheet' type='text/css' href='css/base.css'/>
				<link rel='stylesheet' type='text/css' href='css/layout.css'/>
				<link rel='stylesheet' type='text/css' href='css/skeleton.css'/>
			</head> 
		<body><div class='container'> '''
		# Creating a form variable to contain the html form code
		self.form = ''' 
		<form method='GET'>
			<div class='eight columns'>
				<h1>Phone Book</h1>
				<label for="first_name">First Name</label>
				<input type='text' name='first_name' id='first_name'/>
				<label for="last_name">Last Name</label>
				<input type='text' name='last_name' id='last_name'/>
				<label for="phone_number">Phone Number</label>
				<input type='text' name='phone_number' placeholder='(555) 555-5555' id='phone_number'/>
			</div>
			<div class = 'eight columns'>	
				<select name='phone_type'>
					<option value='phoneType'>Home</option>
			  		<option value='Cell' selected='selected'>Cell</option>
			  		<option value='Work'>Work</option>
				</select>
				<p>Friend</p><input type='checkbox' name='relationship1' value='Friend'/>
				<p>Co-worker</p><input type='checkbox' name='relationship2' value='Co-worker'/>
				<input type='submit' value ='Enter'/>
			</div>	
		</form>	
		'''
		self.footer = '''</div></body></html>'''

	def print_contents(self, i=''):
		if i=='':
			return self.head + self.form + self.footer
		else:
			return self.head + i + self.footer

