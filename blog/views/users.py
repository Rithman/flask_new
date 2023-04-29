from flask import render_template, Blueprint
from werkzeug.exceptions import NotFound
from blog.models.user import User

users_app = Blueprint('users_app', __name__, url_prefix='/users', static_folder='../static')

USERS_LIST = {1: 'admin', 2: 'James', 3: 'Anna', 4: 'Victor', 5: 'Olga'}

@users_app.route('/', endpoint="list")
def render_users():
    users = User.query.all()
    return render_template('users/users_list.html', users_list=users)


@users_app.route('/<int:pk>', endpoint="details")
def user_details(pk:int):
    user = User.query.filter_by(id=pk).one_or_none()
    if user is None:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template('users/details.html', user=user)
