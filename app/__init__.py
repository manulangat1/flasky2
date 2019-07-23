from flask import Flask
#third party imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from config import Config

login = LoginManager()
login.login_view="users.login"
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
#configure image uploading via flask-uploads
# from .models import User



def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(Config)
#     login.init_app(app)
    db.init_app(app)
    # db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    ma.init_app(app)
    from app import models
    # register the blueprint
    from app.users.routes import users
    from app.tasks.routes import tasks
    from app.api.routes import api
    from app.errors.errors import errors
    app.register_blueprint(users)
    app.register_blueprint(tasks)
    app.register_blueprint(api)
    app.register_blueprint(errors)
    return app
