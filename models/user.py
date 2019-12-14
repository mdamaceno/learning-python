from flask_sqlalchemy import SQLAlchemy
from application import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  password = db.Column(db.String(60), nullable=False)
