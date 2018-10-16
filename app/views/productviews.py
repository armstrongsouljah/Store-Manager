from app.utils import bp
from app.models.products import Product
from flask import jsonify
    
@bp.route('/products', methods=['GET'])    
def get_products():   
    response = Product()
    return jsonify(response.get_products())


@bp.route('/products/<int:product_id>')
def get_product(product_id):
    pass



@bp.route('/products/add', methods=['POST'])
def add_product():
    pass

