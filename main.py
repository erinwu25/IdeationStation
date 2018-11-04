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

# class Brainstorm(ndb.model):
#     user_ideas = ndb.StringProperty()
#     recommenda

class MainPage(webapp2.RequestHandler):
    def get(self):
        templateVars = {
        }
        template = env.get_template("index.html")
        self.response.write(template.render(templateVars))

    # def post(self):
    #     templateVars = {
    #         "user_text": user_text;
    #     }
    #     template = env.get_template("index.html")
    #     self.response.write(template.render(templateVars))

class IdeasPage(webapp2.RequestHandler):
    def get(self):
        categories = getCategories(classify_url)
        template = env.get_template("ideas.html")
        user_ideas = self.request.get("user_ideas")

        languages = {'C++': None, 'C': None, 'C#': None, 'Java': None, 'Python': None, 'HTML': None, 'CSS': None,
                    'JavaScript': None, 'MySQL': None, 'Go': None,
        }
        skills = {'mobile': None, 'software': None, 'back-end': None, 'front-end': None, 'machine learning': None,
                    'blockchain': None, 'database': None
        }
        templateVars={
            "categories": categories,
            "user_ideas": user_ideas,
        }
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/ideas", IdeasPage),

], debug=True)
