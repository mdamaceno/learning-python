from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError

class SignupForm(FlaskForm):
  name = StringField('name', [DataRequired()])
  email = StringField('email', [DataRequired(), Email()])
  password = PasswordField('password', [DataRequired(), Length(min=6)])
