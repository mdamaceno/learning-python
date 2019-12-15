from app import db
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(120), nullable=False, unique=True)
  password = db.Column(db.String(60), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return 'User <%r>' % self.id
