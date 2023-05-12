from flask import render_template, request, redirect, url_for, session, flash
from .forms import LoginForm
from app import myapp_obj,db
from app.models import User, Email, Todo
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers
import uuid
import os

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
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
        #find user
        user = User.query.filter_by(username=username).first()
        
        #Either user doesn't exists or password is wrong
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        
        #if all is wel login user and redirect to profile page
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
    
    #first check for duplicate usernames
    if request.method == 'POST': 
        check_username = User.query.filter_by(username=username).first()
        if check_username: 
            flash('Username already in use. Please try another one!')
            return redirect(url_for('register')) 
        #then we can check for phone number
        else:
            user = User.query.filter_by(phonenumber=phonenumber).first()
            #Parse through a phone number;NOTE this only US phone numbers are valid
            try:
                us_number = "+1" + phonenumber
                my_number = phonenumbers.parse(us_number)
            except:
                flash('Not a valid phone number!')
                return redirect(url_for('register'))
            #If the user already exists
            if user: 
                flash('User already exists')
                return redirect(url_for('register'))
            #else if the phonenumber is invalid
            elif not phonenumbers.is_valid_number(my_number): 
                flash('Phone number invalid!')
                return redirect(url_for('register'))
            #Check the length of password 
            if len(password) < 8 or len(password) > 20: 
                flash('Password must be at least 8 characters and no more than 20')
                return redirect(url_for('register'))
            #Must have at least one number 
            elif not any (char.isdigit() for char in password):
                flash('Password must have one number')
                return redirect(url_for('register'))
            
            new_user = User(phonenumber=phonenumber, username=username, password=generate_password_hash(password, method='sha256'))
            #create a new user and add to the database
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')
   
@myapp_obj.route('/resetPassword', methods=['GET', 'POST'])
def resetPassword(): 
    #Forms to reset password. 2 password forms to ensure they match
    username = request.form.get('username')
    phonenumber = request.form.get('phonenumber')
    new_password = request.form.get('new_password')
    new_password2 = request.form.get('new_password2')
    
    
    if request.method == 'POST': 
        #Find user, this time by phonenumber for more security
        user = User.query.filter_by(phonenumber=phonenumber).first()
        
        #user does not exist
        if not user:
            flash('Please check your form details and try again.')
            return redirect(url_for('resetPassword'))
        #username input does not match what we have in the database
        elif username != user.username:
            flash('Username is incorrect! Please try again.')
            return redirect(url_for('resetPassword'))
        #check to see if password input is the same as the old password
        elif check_password_hash(user.password, new_password): 
            flash('New password cannot equal old password.')
            return redirect(url_for('resetPassword'))
        #both password forms must be the same to reset it! 
        elif new_password != new_password2: 
            flash('Passwords must match. Please try again.')
            return redirect(url_for('resetPassword'))
    
        #Then reset the password for our user and save. We don't need to hash it. 
        user.set_password(new_password)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('resetPassword.html')
    
@myapp_obj.route('/deleteAccount', methods=['GET', 'POST'])
@login_required
def delete():
   if request.method == 'POST': 
        #Fetch current user and delete from database
        user = User.query.filter_by(phonenumber= current_user.phonenumber).first()
        #delete all emails user has sent
        emails = Email.query.filter_by(user_id = current_user.id)
        for i in emails:
                db.session.delete(i)
                db.session.commit()
        todos = Todo.query.filter_by(user_id = current_user.id)
        for i in todos:
                db.session.delete(i)
                db.session.commit()
        #delete user, and save                
        db.session.delete(user)
        db.session.commit()
        flash("Your account has been deleted")
        return redirect(url_for('login'))
    
   return render_template('deleteAccount.html')


UPLOAD_FOLDER = 'myapp/static/images/profile'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@myapp_obj.route('/upload_profile_picture', methods=['GET', 'POST'])
@login_required
def upload_profile_picture():
    form = ProfilePictureForm()
    if form.validate_on_submit():
        file = form.profile_picture.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            
            # Update the user's profile picture field in the database
            current_user.profile_picture = file_path
            db.session.commit()
            
            flash('Profile picture uploaded successfully!')
            return redirect(url_for('profile'))
    return render_template('upload_profile_picture.html', form=form)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@myapp_obj.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

@myapp_obj.route('/inbox',methods=['GET','POST'])
@login_required
def inbox(): 
    #contains compose, searchbar
        emails = Email.query.filter_by(user_id = current_user.id)
        if request.method == 'POST':
                emails = Email.query.filter_by(user_id = current_user.id, subject = request.form.get('searchoption'))
        return render_template('inbox.html',emails = emails) 
    
@myapp_obj.route('/emailReader/<id>',methods=['GET','POST'])
def emailReader(id):
        email = Email.query.filter_by(id=id).first()
        return render_template('emailReader.html',email=email)

@myapp_obj.route('/composer',methods=['GET','POST'])
@login_required
def composer():
        recipient = request.form.get('recipient')
        subject = request.form.get('subject')
        msg = request.form.get('msg')
        if request.method == 'POST':
                new_email = Email(recipient = recipient, subject = subject, msg = msg)
                #new_email.sender = current_user.username
                users = User.query.all()
                uid = "null"
                for i in users:
                        if i.username == recipient:
                                uid = i.id
                new_email.user_id = uid
                if uid == "null":
                        flash("The user you entered does not exist")
                        return redirect(url_for('composer'))
                db.session.add(new_email)
                db.session.commit()
                flash("The email has been sent")
                return redirect('/inbox')
        return render_template('composer.html')
    
@myapp_obj.route('/delete_email/<id>')
def delete_email(id):
        email=Email.query.filter_by(id=id).first()
        db.session.delete(email)
        db.session.commit()
        return redirect('/inbox')

@myapp_obj.route('/todolist')
@login_required
def todolist():

        incomplete = Todo.query.filter_by(complete=False,user_id = current_user.id).all()
        complete = Todo.query.filter_by(complete=True,user_id = current_user.id).all()
        return render_template('todolist.html', incomplete=incomplete, complete=complete)

@myapp_obj.route('/add', methods=['GET','POST'])
def add():
        
        text = request.form['todoitem']
        if text.isspace() or text == "":
                flash('Please type the task you would like to add')
                return redirect(url_for('todolist'))
        todo = Todo(text=request.form['todoitem'], complete=False,user_id = current_user.id)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todolist'))

@myapp_obj.route('/complete/<id>')
def complete(id):

        todo = Todo.query.filter_by(id=int(id)).first()
        todo.complete = True
        db.session.commit()
        return redirect(url_for('todolist'))

@myapp_obj.route('/clearTodo', methods=['GET','POST'])
def clearTodo():

        todo = Todo.query.filter_by(complete=True, user_id = current_user.id)
        for i in todo:
                db.session.delete(i)
                db.session.commit()
        return redirect(url_for('todolist'))
