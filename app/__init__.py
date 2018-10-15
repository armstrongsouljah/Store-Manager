import os
from flask import Flask, jsonify
from app.api import bp
from app.models.sales import Sale
from app.models.products import Product
from .config import env_config

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(env_config.get(config_name))
    app.config.from_pyfile(os.path.join(basedir, 'config.py'))
    return app


@bp.route('/products', methods=['GET'])
def get_products():
    obj = Product()
    return obj.get_products()


@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    pass


@bp.route('/sales', methods=['GET'])
def get_sales():
    return jsonify({"message":"hello sales"})


@bp.route('/sales/<int:sales_id>')
def get_sale(sales_id):
    pass

@bp.route('/products/add', methods=['POST'])
def add_product():
    pass


@bp.route('/sales/add', methods =['POST'])
def add_sale():
    pass


# register blueprint in the app factory
app = create_app('development')
app.register_blueprint(bp, url_prefix='/api/v1')

