# Samantha Miller
# March 10, 2014
# Serverside Form



#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
# From the python file form import the class Form
from form import Form

class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.GET:
			# Creating empty sting variable that will later be used to populate form values onto the page.
			relationship = ''
			# Using try: to prevent checkbox errors
			try:
				# Set relationship_type equal to the value of the 'relationship1' checkbox if checked
				relationship_type = self.request.GET['relationship1']
				# If the person did check the 'relationship1' checkbox 
				if relationship_type:
					# Then set empty string variable equal to itself plus the new relationship variable type which will be equal to the checkbox 'relationship1'
					relationship = relationship + relationship_type + ' '	
			# If they check neither box no error will happen			
			except StandardError:
				pass
			# Using try: to prevent checkbox errors
			try:
				# Set relationshiip_type2 equal to the value of the "relationship2" checkbox if checked
				relationship_type2 = self.request.GET['relationship2']
				# If the person did check the 'relationship2' checkbox
				if relationship_type2:
					# Then set empty string variable equal to itself plus the new relationship variable type which will be equal to the checkbox 'relationship2'
					# Also because of this both can be checked 
					relationship = relationship + relationship_type2
			# If they check neither box no error will happen		
			except StandardError:
				pass
			# Set variable form_info equal to all the user inputed form information
			form_info = self.request.GET['first_name'] + ' ' + self.request.GET['last_name'] + ' ' + self.request.GET['phone_type'] + ' ' + self.request.GET['phone_number'] + ' ' + relationship
			# Creates form Object
			form = Form(self) 
			# Will populate the user inputed information on a new Form Page
			self.response.write(form.print_contents(form_info))
		else:
			# Creates form Object
			form = Form(self)
			# Will populate the form for the user to input it's information
			self.response.write(form.print_contents())
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)