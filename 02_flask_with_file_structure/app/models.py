from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phonenumber = db.Column(db.String(100), nullable=False)

    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}>'
    
    def remove(self):
        db.session.delete(self)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    recipient_id =  db.Column(db.Integer(), db.ForeignKey('user.id')
    message_body  = db.Column(db.String(255))
    create_date = db.Column(db.Integer(), default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Message {self.id}: {self.message_body}>'


