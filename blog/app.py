from flask import Flask, render_template
import os

from .users.views import users_app
from .index.views import index_app
from .articles.views import articles_app
from .auth.views import auth_app, login_manager
from blog.models.database import db



def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(users_app)
    app.register_blueprint(index_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app, url_prefix="/auth")

    app.config["SECRET_KEY"] = "1235nkm45098ssdug092k301"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)

    return app


