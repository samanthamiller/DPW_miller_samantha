import webapp2
from details import Details

class MainHandler(webapp2.RequestHandler):
    def get(self):
        details = Details()
        self.response.write(details.header)
        self.response.write(details.body)
        self.response.write(details.footer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
