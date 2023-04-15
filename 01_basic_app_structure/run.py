# app is a variable inside the file __init__.py in side of
# the app_folder directory.
from flask import Flask
from flask import escape

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    return "home"

@myapp_obj.route("/hello")
def hello():
    return "Hello World!"

@myapp_obj.route("/login")
def login():
    return "Login Page!"

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

myapp_obj.run()
