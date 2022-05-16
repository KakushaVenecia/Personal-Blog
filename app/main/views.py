
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort,flash

from app.auth.forms import LoginForm
from . import main
import requests
from .forms import SubscribeForm, BlogForm
from ..models import *

@main.route('/')
def index():
    random_quotes = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    response = random_quotes.json()
    subscribeform = SubscribeForm()
    return render_template('/index.html' , response =response , subscribeform =subscribeform)

@main.route('/random_quotes',methods=['GET','POST'])
def json():
    return render_template('random_quotes.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/subscribe')
def subscriber():
    return render_template('subscribe.html')

@main.route('/dashboard', methods=['GET','POST'])
@login_required
def blog():
    blogform =BlogForm()
    if blogform.validate_on_submit():
        
        blog = Blog(title=blogform.title.data, post=blogform.post.data, category=blogform.category.data)

        db.session.add(blog)
        db.session.commit()
        flash('Thanks for your post!')
        return redirect(url_for('main.index'))
    
    return render_template('dashboard.html',blogform=blogform)
