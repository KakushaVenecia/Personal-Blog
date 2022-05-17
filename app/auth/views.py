from app.main.forms import BlogForm
from . import auth
from flask import render_template,redirect,url_for, flash,request
from ..models import User, Blog
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm, RegistrationForm, AdminForm


# @auth.route('/auth/login',methods=['GET','POST'])
# def login():
#     login_form = LoginForm()
#     if login_form.validate_on_submit():
#         user = User.query.filter_by(email = login_form.email.data).first()
#         if user is not None and user.verify_password(login_form.password.data):
#             login_user(user,login_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))

#         flash('Invalid username or Password')

#     title = "login"
#     return render_template('auth/login.html',login_form = login_form, title=title)
    

@auth.route('/auth/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
 
        # mail_message("Welcome to Pitcher App!","email/email", user.email, user=user)
        return redirect(url_for('auth.login'))
        
    title = "New Account"
    return render_template('/auth/register.html',form = form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/auth/login',methods=['GET','POST'])
def login_admin():
    login_form = LoginForm()
    # blogform= BlogForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
    title = "New Account"
    return render_template('/auth/login-admin.html',login_form = login_form, title = title)

     
@auth.route('/auth/logout-admin')
@login_required
def logout_admin():
    logout_user()
    return redirect(url_for("main.index"))