from . import  db,login
from flask import current_app
from datetime import datetime
#flask import
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
#create your odel classes here
class  User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),index=True,unique=True)
    email = db.Column(db.String(128),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140),index=True)
    tasks = db.relationship('Task',backref="author",lazy="dynamic")
    last_seen = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self,password):
        self.password_hash= generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

#defines the user loader function
@login.user_loader
def load_user(id):
    user = User.query.get(int(id))
    return user
#task model
class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),index=True)
    details = db.Column(db.String(120))
    image_filename = db.Column(db.String(),default=None,nullable=True)
    image_url = db.Column(db.String,default=None,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<User {}>'.format(self.name)
