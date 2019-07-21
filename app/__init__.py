from flask import Flask
#third party imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_uploads import UploadSet,IMAGES,configure_uploads
#local import ie live in the same dir
from config import Config

#initialising the app
# app = Flask(__name__, static_url_path='/static')
# app.config.from_object(Config)
login = LoginManager()
login.login_view="users.login"
db = SQLAlchemy()
migrate = Migrate()
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
    from app import models
    # register the blueprint
    from app.users.routes import users
    app.register_blueprint(users)
    return app
