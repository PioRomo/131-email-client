from app import myapp_obj
from flask import escape

@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    return "hi"

@myapp_obj.route("/hello")
def hello():
    return "Hello World!"

@myapp_obj.route("/login")
def login():
    return "Login Page!"

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
