from flask import render_template, request, redirect, url_for, flash
import bcrypt
from app import app, db
from myapp.models.user import User
from myapp.forms.signup import SignupForm

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  inputs = SignupForm(request.form)
  # POST: Create user
  if request.method == 'POST':
    # Validation
    if inputs.validate():
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
          password=bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('dashboard'))
      flash('A user already exists with that email address.')
      return redirect(url_for('signup'))
  # GET: Serve sign up page
  form = SignupForm()
  return render_template('signup.html', form=SignupForm())

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/user')
def user():
  return render_template('user.html')
