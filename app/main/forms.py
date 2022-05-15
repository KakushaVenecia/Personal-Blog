from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired ,Email

class AdminForm(FlaskForm):
    username = StringField('Your Username',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    submit = SubmitField('Sign In')


class UserForm(FlaskForm):
    username = StringField('Your Username',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SubscribeForm(FlaskForm):
    email = StringField('Your Username',validators=[DataRequired(),Email()])
    submit = SubmitField('Subscribe')