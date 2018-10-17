import os
from flask import Flask
from app.models.products import Product
from app.models.sales import Sale
from app.views.productviews import *
from app.views.salesviews import *
from .config import env_config
from .utils import bp,  welcome_message
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# bp = Blueprint('api', __name__)


def create_app_environment(config_name):
    """ allows one to switch environments """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(env_config.get(config_name))
    app.config.from_pyfile(os.path.join(BASE_DIR, 'config.py'))
    return app


app = create_app_environment('development')
jwt = JWTManager(app)
# welcome route
@app.route("/", methods=["GET"])
def index():
    return welcome_message

# register blueprint in the app factory
app.register_blueprint(bp, url_prefix='/api/v1')
