from flask import render_template, Blueprint

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')

USERS_LIST = {1: 'John', 2: 'Sergey', 3: 'Anna', 4: 'Victor', 5: 'Olga'}

@users.route('/')
def render_users():
    return render_template('users/users_list.html', users_list=USERS_LIST)


@users.route('/<int:pk>')
def render_user_by_pk(pk:int):
    return render_template('users/user.html', user=USERS_LIST[pk])
