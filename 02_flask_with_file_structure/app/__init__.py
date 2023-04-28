from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from flask_login import LoginManager

myapp_obj = Flask(__name__)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)


db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)
login.login_view = 'login'

from app import routes, models

with myapp_obj.app_context():
    db.create_all()

from app.models import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

