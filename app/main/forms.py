from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired ,Email

class AdminForm(FlaskForm):
    username = StringField('Your Username',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    submit = SubmitField('Sign In')

class BlogForm(FlaskForm):
    title = StringField ('Blog Title', validators =[DataRequired()])
    post= TextAreaField ('Write away', validators=[DataRequired()])
    category=StringField('Category',validators = [DataRequired()])
    submit = SubmitField('Publish')

class SubscribeForm(FlaskForm):
    email = StringField('Your Username',validators=[DataRequired(),Email()])
    submit = SubmitField('Subscribe')