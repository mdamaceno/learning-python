from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html', thing_to_say='hello')

@app.route('/signin')
def sing_in():
  return render_template('sign_in.html')

@app.route('/signup')
def sing_up():
  return render_template('sign_up.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/user')
def user():
  return render_template('user.html')
