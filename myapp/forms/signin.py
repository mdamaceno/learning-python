from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

class SigninForm(FlaskForm):
  email = TextField('email')
  password = PasswordField('password')
