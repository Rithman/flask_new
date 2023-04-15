from flask import render_template, Blueprint

index = Blueprint('index', __name__, url_prefix='/', static_folder='../static')




@index.route('/')
def render_index():
    return render_template('index/index.html')
