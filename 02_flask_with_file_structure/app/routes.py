from flask import render_template, request, redirect, url_for, session, flash
from .forms import LoginForm
from app import myapp_obj
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers
import re 


from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required


@myapp_obj.route("/")
@myapp_obj.route("/index.html")           
def index():
    name = 'Carlos'
    books = [ {'author': 'authorname1',
                'book':'bookname1'},
             {'author': 'authorname2',
              'book': 'bookname2'}]
    return render_template('hello.html',name=name, books=books)

#login method
@myapp_obj.route("/login", methods =['GET', 'POST'])
def login():
    return render_template('login.html', msg = msg)
 
#logout method
@myapp_obj.route("/logout")
def logout():
    return redirect(url_for('login'))

#register method
@myapp_obj.route("/register", methods =['GET', 'POST'])
def register():
    return render_template('register.html', msg = msg)
