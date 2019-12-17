from flask import Flask
from .models import db

def create_app():
  app = Flask(__name__)
  app.config.from_pyfile('config.py')

  db.init_app(app)

  from core.auth.routes import auth

  app.register_blueprint(auth)

  return app
