from flask import Flask, render_template

from .users.views import users
from .index.views import index
from .articles.views import articles



def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(users)
    app.register_blueprint(index)
    app.register_blueprint(articles)
    return app


