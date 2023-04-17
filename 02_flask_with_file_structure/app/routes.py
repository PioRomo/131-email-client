from flask import render_template, request, redirect, url_for, session, flash
from .forms import LoginForm
from app import myapp_obj
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers


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
@myapp_obj.route("/login")
def login():
    return render_template('login.html')
 
#logout method
@myapp_obj.route("/logout")
def logout():
    return redirect(url_for('login'))

#register method
@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route('/deleteAccount', methods=['GET', 'POST'])
@login_required
def delete():
    current_user.remove()
    db.session.commit()
    flash('You are no longer exist')
    return render_template('deleteAccount.html')
