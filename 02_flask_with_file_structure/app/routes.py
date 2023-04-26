from flask import render_template, request, redirect, url_for, session, flash
from .forms import LoginForm
from app import myapp_obj,db
from app.models import User
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/")
@myapp_obj.route('/hello')           
def hello():
    return render_template('hello.html')

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    if request.method == 'POST': 
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('profile'))
    return render_template('login.html')
        
  
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
    
        try:
            us_number = "+1" + phonenumber
            my_number = phonenumbers.parse(us_number)
            
        except:
            flash('Not a valid phone number!')
            return redirect(url_for('register'))
        if user: 
            flash('User already exists')
            return redirect(url_for('register'))
        
        elif not phonenumbers.is_valid_number(my_number): 
            flash('Phone number invalid!')
            return redirect(url_for('register'))
        
        if len(password) < 8 or len(password) > 20: 
            flash('Password must be at least 8 characters and no more than 20')
            return redirect(url_for('register'))
        elif not any (char.isdigit() for char in password):
            flash('Password must have one number')
            return redirect(url_for('register'))
            
        new_user = User(phonenumber=phonenumber, username=username, password=generate_password_hash(password, method='sha256'))
       #new_user.set_password(new_user.password)
        db.session.add(new_user)
        db.session.commit()
        flash('Redirecting.....')
        return redirect(url_for('login'))
     
    return render_template('register.html')
   
    
    
@myapp_obj.route('/deleteAccount', methods=['GET', 'POST'])
@login_required
def delete():
   if request.method == 'POST': 
        user = User.query.filter_by(phonenumber= current_user.phonenumber).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('login'))
    
   return render_template('deleteAccount.html')

@myapp_obj.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
