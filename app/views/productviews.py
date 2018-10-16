from app.utils import bp, welcome_message
from app.models.products import Product
from flask import jsonify


obj = Product()


@bp.route("/", methods=["GET"])
def index():
    return welcome_message
    
@bp.route('/products', methods=['GET'])    
def get_products():        
    return jsonify(obj.get_products())


@bp.route('/products/<int:product_id>')
def get_product(product_id):
    pass



@bp.route('/products/add', methods=['POST'])
def add_product():
    pass

