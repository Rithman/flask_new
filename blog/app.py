from flask import Flask
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


from .views.users import users_app
from .views.index import index_app
from .views.articles import articles_app
from .views.auth import auth_app, login_manager
from blog.models.database import db
from blog.security import flask_bcrypt


load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(users_app)
    app.register_blueprint(index_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app, url_prefix="/auth")


    app.config["SECRET_KEY"] = 'abcdefg123456'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")
    
    login_manager.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)

    flask_bcrypt.init_app(app)

    return app



