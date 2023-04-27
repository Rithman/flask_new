from flask import render_template, Blueprint

index_app = Blueprint('index', __name__, url_prefix='/', static_folder='../static')




@index_app.route('/')
def render_index():
    return render_template('index/index.html')
