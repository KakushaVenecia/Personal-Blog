from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
import requests
from .forms import AdminForm 


@main.route('/')
def index():
    random_quotes = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    response = random_quotes.json()
    return render_template('/index.html' , response =response )

@main.route('/random_quotes',methods=['GET','POST'])
def json():
    return render_template('random_quotes.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/admin')
# @login_required
def admin():
    adminform = AdminForm()
    return render_template('/admin.html', adminform = adminform)



# @main.route('/post/<int:post_id>')
# def post(post_id):
#     post = ('kajhdkahdjkhakjdhjka').query.filter_by(id=post_id).one()

#     return render_template('post.html', post=post)

# @main.route('/add')
# def add():
#     return render_template('add.html')

# @main.route('/addpost', methods=['POST'])
# def addpost():
#     title = request.form['title']
#     subtitle = request.form['subtitle']
#     author = request.form['author']
#     content = request.form['content']

#     post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

#     db.session.add(post)
#     db.session.commit()

#     return redirect(url_for('index'))