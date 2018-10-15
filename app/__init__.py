from flask import Flask, jsonify
from app.api import bp
from app.models.sales import Sale
from app.models.products import Product


app = Flask(__name__)


@bp.route('/products', methods=['GET'])
def get_products():
    return jsonify({"message":"hello products"})


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
app.register_blueprint(bp, url_prefix='/api/v1')

