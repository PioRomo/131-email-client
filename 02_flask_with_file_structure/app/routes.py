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

@myapp_obj.route("/register", methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    phonenumber = request.form.get('phoneNumber')
    
    user = User.query.filter_by(phonenumber=phonenumber).first()
    
    my_number = phonenumbers.parse(phonenumber)
    if phonenumbers.is_valid_number(my_number):
        if user: 
        flash('Email address already exists')
        return redirect(url_for('register'))
    
    new_user = User(phonenumber=phonenumber, name=name, password=generate_password_hash(password, method='sha256'))
    
    db.session.add(new_user)
    db.session.commit()
    else:
        flash('Invalid phone number!')
   
    
    
     

@myapp_obj.route('/deleteAccount', methods=['GET', 'POST'])
@login_required
def delete():
    current_user.remove()
    db.session.commit()
    flash('You are no longer exist')
    return render_template('deleteAccount.html')
