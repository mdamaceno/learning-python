from flask import render_template, request, redirect
import bcrypt
from app import db
from myapp.models.user import User
from myapp.forms.signup import *

def index():
  return render_template('home.html')

def signin():
  return render_template('signin.html')

def signup():
  if request.method == 'POST':
    user = User(
      name=request.form['name'],
      email=request.form['email'],
      password=bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt())
    )

    db.session.add(user)
    db.session.commit()

  form = SignupForm()
  return render_template('signup.html', form=form)

def dashboard():
  return render_template('dashboard.html')

def user():
  return render_template('user.html')
