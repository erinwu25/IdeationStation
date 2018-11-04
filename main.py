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

        template = env.get_template("ideas.html")
        user_ideas = self.request.get("user_ideas")
        categories = getCategories(classify_url, user_ideas)

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

def getCategories(url, user_ideas): #url is unique to categories function in api

	data = {
	   "document": {
	      "type": "PLAIN_TEXT",
	      "language": "EN",
	      "content": user_ideas,
	    }
	}

	headers = {
	   "Content-Type" : "application/json; charset=utf-8"
	}

	jsondata = json.dumps(data)
	result = urlfetch.fetch(url, method=urlfetch.POST, payload=json.dumps(data), headers=headers)
	python_result = json.loads(result.content)
	string = ""
	if 'categories' in python_result:
	       for i in range(0, len(python_result["categories"])):
	              string += "Your ideas indicates that you might want to: "
	              string += python_result["categories"][i]["name"]
	              string += " category with a "
	              string += str(python_result["categories"][i]["confidence"])
	              string += " level of confidence. \n"
	       return string
	else:
	       return 'Not enough data'



app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/ideas", IdeasPage),

], debug=True)
