class Form():
	# Init function that will run when the page is opened 
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
			<div class='sixteen columns'>
				<h1>Phone Book</h1>
			</div>	
			<div class='eight columns' id='first_column'>	
				<label for="first_name">First Name</label>
				<input type='text' name='first_name' id='first_name'/>
				<label for="last_name">Last Name</label>
				<input type='text' name='last_name' id='last_name'/>
				<label for="phone_number">Phone Number</label>
				<input type='text' name='phone_number' placeholder='(555) 555-5555' id='phone_number'/>
			</div>
			<div class = 'eight columns' id='second_column'>
				<p class='label'>Select Phone Type</p>	
				<select name='phone_type'>
					<option value='phoneType'>Home</option>
			  		<option value='Cell' selected='selected'>Cell</option>
			  		<option value='Work'>Work</option>
				</select>
				<p class='label'>Relationship</p>
				<input type='checkbox' name='relationship1' value='Friend'/><p>Friend</p>
				<input type='checkbox' name='relationship2' value='Co-worker'/><p>Co-worker</p> <br>
				<input type='submit' value ='Enter' id='button'/>
			</div>	
		</form>	
		'''
		# Creating a footer variable to contain the end the html code of the page
		self.footer = '''</div></body></html>'''
	# Function to print the contents of this page
	def print_contents(self, i=''):
		# If i is empty populate the form for the user to input their information
		if i=='':
			return self.head + self.form + self.footer
		# If the form has been filled out populate what the user entered	
		else:
			return self.head + i + self.footer