from flask import render_template, request, redirect
import bcrypt
from app import db
from myapp.models.user import User

def index():
  return render_template('home.html')

def sign_in():
  return render_template('sign_in.html')

def sign_up():
  if request.method == 'POST':
    user = User(
      name=request.form['name'],
      email=request.form['email'],
      password=bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt())
    )

    db.session.add(user)
    db.session.commit()

  return render_template('sign_up.html')

def dashboard():
  return render_template('dashboard.html')

def user():
  return render_template('user.html')
