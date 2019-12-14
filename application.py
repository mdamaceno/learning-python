from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(120), nullable=False, unique=True)
  password = db.Column(db.String(60), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return 'User <%r>' % self.id

@app.route('/')
def hello_world():
  return render_template('home.html')

@app.route('/signin')
def sign_in():
  return render_template('sign_in.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    user = User(
      name=request.form['name'],
      email=request.form['email'],
      password=bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt())
    )

    try:
      db.session.add(user)
      db.session.commit()

      return redirect('/')
    except Exception as e:
      raise e

  return render_template('sign_up.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/user')
def user():
  return render_template('user.html')

if __name__ == '__main__':
  app.run(debug=True)
