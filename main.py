import webapp2
import jinja2
import os
import logging
import time

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        templateVars = {
        }
        template = env.get_template("index.html")
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", MainPage),

], debug=True)
