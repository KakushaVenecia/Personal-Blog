from datetime import datetime
from click import pass_context
from sqlalchemy import false
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='user')
   
    
    @property
    def password(self):
        raise AttributeError('You cant read the password')

    @password.setter
    def password(self, password):
        self.password_hash =generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'


class Blog(UserMixin, db.Model):
    __tablename__= 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    post= db.Column(db.String(255))
    category=db.Column(db.String(255))
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'),nullable=False)
    comments = db.relationship('Comment', backref='blog', lazy = 'dynamic')
       

class Admin(UserMixin,db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    blog = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ ='comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(255))
    date = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    
    
