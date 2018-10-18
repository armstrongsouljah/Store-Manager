from app.utils import bp
from app.models.products import Product
from app.models.users import User
from flask import jsonify, request
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)

product_model = Product()
user1 = User(1,"armstrong", True, "hello")


    
@bp.route('/products', methods=['GET'])    
def get_products():
    response  = product_model.get_products()
    return jsonify(response)

@bp.route('/products', methods=['POST'])
@jwt_required
def products_add():
    user = get_jwt_identity()
    if user == 'admin':
        response = product_model.add_product()
        return jsonify(response), 200
    return jsonify(message="Acess denied for non admins"), 401


@bp.route('/products/<int:productId>')
def get_product(productId):
    response = product_model.get_product(productId)
    return jsonify(response)

