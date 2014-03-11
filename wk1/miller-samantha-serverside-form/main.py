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
from form import Form

class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.GET:
			relationship = ''
			try:
				relationship_type = self.request.GET['relationship1']
				if relationship_type:
					print relationship_type
					relationship = relationship + relationship_type + ' '
			except StandardError:
				pass

			try:
				relationship_type2 = self.request.GET['relationship2']
				if relationship_type2:
					print relationship_type2
					relationship = relationship + relationship_type2
			except StandardError:
				pass
			
			form_info = self.request.GET['first_name'] + ' ' + self.request.GET['last_name'] + ' ' + self.request.GET['phone_number'] + ' ' + self.request.GET['phone_type'] + ' ' + relationship
			form = Form(self) #Creates form Object
			self.response.write(form.print_contents(form_info))
		else:
			form = Form(self) #Creates form Object
			self.response.write(form.print_contents())
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)