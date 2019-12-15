from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class SignupForm(FlaskForm):
  name = StringField('name')
  email = StringField('email')
  password = PasswordField('password')
