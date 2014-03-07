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
from page import Page 
#importing additional code, what handles going to a browser

# Master class
class MainHandler(webapp2.RequestHandler):
	# Unique to framework
	# this function runs first #catalyst
	def get(self):
		# Start writing code  
		if self.request.GET:
			info = self.request.GET['first_name'] + ' ' +self.request.GET['last_name']
			page = Page() # Creates a page object
			self.response.write(page.print_contents(info))
		else:
			page = Page() # Creates a page object
			self.response.write(page.print_contents())
			pass

#associates class with framework
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
