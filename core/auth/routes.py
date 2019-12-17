from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .forms.signup import SignupForm
from .forms.signin import SigninForm
from core.models import db, User

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth.route('/signin')
def signin():
  return render_template('auth/signin.html', form=SigninForm())

@auth.route('/signup')
def signup():
  # GET: Serve sign up page
  form = SignupForm()
  return render_template('auth/signup.html', form=SignupForm())

@auth.route('/register', methods=['POST'])
def register():
  signup_form = SignupForm(request.form)
  if signup_form.validate():
    # Get form fields
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user is None:
      # Save the user
      user = User(
        name=name,
        email=email,
        password=generate_password_hash(password, method='sha256')
      )
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('auth.signin'))
    flash('A user already exists with that email address.')
    return redirect(url_for('auth.signup'))

@auth.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  user = User.query.filter_by(email=email).first()
  # Check if user exists and if password is right
  if user is not None and check_password_hash(user.password, password):
    login_user(user)
    return redirect(url_for('admin.dashboard'))
  # Redirect if credentials is wrong
  flash('Please check your login details and try again.')
  return redirect(url_for('auth.signin'))
