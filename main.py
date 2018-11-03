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
        # fetch that question, and return that key and pass as a template variable.
        template = env.get_template("index.html")
        templateVars = {
        }
        self.response.write(template.render(templateVars))
