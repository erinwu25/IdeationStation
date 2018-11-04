import webapp2
import jinja2
import os
import time
import argparse
import io
import json
import StringIO
import urllib
#^unsure if those last three imports are needed but the docs said they were

#import apis from google appengine
from google.appengine.api import urlfetch
from google.appengine.ext import ndb

#import classify function from language apis
API_KEY = "AIzaSyAAJVm5_VGMef71NmctVuM9H0ShUoAEq3o"
classify_url = "https://language.googleapis.com/v1/documents:classifyText?key=" + API_KEY


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

    def post(self):
        templateVars = {
            "user_text": user_text;
        }
        template = env.get_template("index.html")
        self.response.write(template.render(templateVars))

class IdeasPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("ideas.html")
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/ideas", IdeasPage),

], debug=True)
