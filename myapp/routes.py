from app import app
from myapp.controllers import users_controller

app.add_url_rule('/', 'home', view_func=users_controller.index)
app.add_url_rule('/signin', 'sign_in', view_func=users_controller.sign_in)
app.add_url_rule('/signup', 'sign_up', view_func=users_controller.sign_up, methods=['GET', 'POST'])
app.add_url_rule('/dashboard', 'dashboard', view_func=users_controller.dashboard)
app.add_url_rule('/user', 'user', view_func=users_controller.user)
