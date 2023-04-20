from flask import render_template, request, redirect, url_for, session, flash
from .forms import LoginForm
from app import myapp_obj
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

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

@myapp_obj.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(phonenumber=phonenumber).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login')) 

    login_user(user, remember=remember)
    return redirect(url_for('profile'))
 
#logout method
@myapp_obj.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    phonenumber = request.form.get('phonenumber')
    
    if request.method == 'POST': 
        user = User.query.filter_by(phonenumber=phonenumber).first()
    
        my_number = phonenumbers.parse(phonenumber)
        if user: 
            flash('User already exists')
            return redirect(url_for('register'))
        
        elif not phonenumbers.is_valid_number(my_number): 
            flash('Phone number invalid!')
            return redirect(url_for('register'))
            
        new_user = User(phonenumber=phonenumber, name=name, password=generate_password_hash(password, method='sha256'))
        new_user.set_password(new_user.password)
        db.session.add(new_user)
        db.session.commit()
        flash('Redirecting.....')
        return redirect(url_for('login'))
     
    return render_template('register.html')
   
    
    
@myapp_obj.route('/deleteAccount', methods=['GET', 'POST'])
@login_required
def delete():
    current_user.remove()
    db.session.commit()
    flash('You are no longer exist')
    return render_template('deleteAccount.html')

@myapp_obj.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
