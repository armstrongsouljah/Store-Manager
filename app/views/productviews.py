from app.utils import bp
from app.models.products import Product
from app.models.users import User
from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)

product_model = Product()

class ProductsView(MethodView):
    def __init__(self):
        self.current_user = get_jwt_identity()

    def get(self, productId=None):
        if productId:
            response = product_model.get_product(productId)
            return jsonify(response)
        else:
            response = product_model.get_products
            return jsonify(response)
            
    def post(self):
        if self.current_user == 'admin':
            response = product_model.add_product()
            return jsonify(response), 200
        return jsonify(message="Acess denied for non admins"), 401

    def put(self, productId):
        if self.current_user == 'admin':
            response = product_model.update_product_details(productId)
            return jsonify(response),201
        return jsonify(response="Admin access only"), 401
        
    
    def delete(self, productId):
        if self.current_user == 'admin':
            response = product_model.delete_from_store(productId)
        else:
            response = {"msg":"Only admins can delete a product"}, 401
        return jsonify(response)
  