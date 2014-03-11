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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        self.luke = Character()
        self.luke.name = 'Luke Skywalker'
        self.luke.age = 19
        self.luke.profession = 'Jedi Knight'

        self.leia = Character()
        self.leia.name = 'Leaia Organa'
        self.leia.age = self.luke.age
        self.leia.profession = 'princess'

        self.yoda = Character()
        self.yoda.name = 'Master Yoda'
        self.yoda.age = 896
        self.yoda.profession = 'Jedi'

class Character():
	def __init__(self):
		# Default values assigned here
		self.name = ''
		self.age = 0
		self.profession = ''

	def fight(self):	


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
