import webapp2
import jinja2
import os
import time
import argparse
import io
import json
#^unsure if those last three imports are needed but the docs said they were

from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums
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
