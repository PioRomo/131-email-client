from flask import render_template, request, redirect, url_for, session, flash
from .forms import LoginForm
from app import myapp_obj
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers
import re 
import MySQLdb.cursors

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
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
 
#logout method
@myapp_obj.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

#register method
@myapp_obj.route("/register", methods =['GET', 'POST'])
def register():
         
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'phone number' in request.form :
        username = request.form['username']
        password = request.form['password']
        phoneNumber = request.form['phone number']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        p = phonenumbers.parse(phoneNumber)
        if account:
            msg = 'Account already exists !'
        elif not phonenumbers.is_valid_number(p): 
            msg = "Phone Number is invalid!"
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not phoneNumber:
            msg = 'Please fill out the form yay!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)
