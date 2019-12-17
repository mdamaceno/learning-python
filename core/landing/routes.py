from flask import Blueprint, render_template

landing = Blueprint('landing', __name__, template_folder='templates', static_folder='static')

@landing.route('/')
def index():
  return render_template('home.html')
