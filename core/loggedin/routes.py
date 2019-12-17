from flask import Blueprint, render_template

loggedin = Blueprint('loggedin', __name__, template_folder='templates', static_folder='static')

@loggedin.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@loggedin.route('/user')
def user():
  return render_template('user.html')
