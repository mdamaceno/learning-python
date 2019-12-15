from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

template_dir = os.path.abspath('./myapp/templates')
static_dir = os.path.abspath('./myapp/static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from myapp.routes import *

if __name__ == '__main__':
  app.run()
