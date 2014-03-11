import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	# self.attribute - without 'self' it is a variable local to the function
    	self.t = Transcript()
    	self.t.grade1 = 90
    	self.t.grade2 = 94
    	self.t.quiz1 = 72
    	self.t.quiz2 = 95
    	self.t.calc_grade() #run the calc grade function
    	print self.t.final_grade
    	# self.t.final_grade = self.t.calc_grade()
    	# To access the property function


# The 'object' inhearatince is important
class Transcript(object):
	def __init__(self):
		self.grade1 = 0
		self.grade2 = 0
		self.quiz1 = 0
		self.quiz2 = 0
		self.__final_grade = 0

		# public
		# _ protected
		# __ private

		# Make final_grade a property with the '@property' decorator
	@property
	def final_grade(self):
		return str(self.__final_grade) + ' is your final grade.'


	def calc_grade(self):
		avg = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2)/4
		self.__final_grade = avg

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
