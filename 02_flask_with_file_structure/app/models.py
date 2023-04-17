from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    posts = db.relationship('Post', backref='author', lazy='dynamic')

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
    subject = db.Column(db.varchar2(100))
    creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    parent_message_id = db.Column(db.Integer(), nullable=True, db.ForeignKey('message.id') )
    message_body  = db.Column(db.clob)
    create_date = db.Column(db.Integer(), default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Message {self.id}: {self.message_body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
