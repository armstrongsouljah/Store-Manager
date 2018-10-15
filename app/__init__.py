import os
from flask import Flask, jsonify
from app.api import bp

from app.models.products import Product
from app.models.sales import Sale
from app.views.productviews import *
from app.views.salesviews import *

from .config import env_config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(env_config.get(config_name))
    app.config.from_pyfile(os.path.join(BASE_DIR, 'config.py'))
    return app


# register blueprint in the app factory
app = create_app('development')
app.register_blueprint(bp, url_prefix='/api/v1')
