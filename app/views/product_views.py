from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, get_raw_jwt
from app.models.products import Product
from app.utils import fetch_all, check_item_exists
from databases.server import DatabaseConnection
product_obj = Product()
cursor = DatabaseConnection().cursor

class ProductsView(MethodView):
    """ Enables the admin user to add a product to the store """

    def get(self, productId=None):
        """
        tags:
           - Products
        summary: Returns a list of products in json format
        responses:
          '200':
             description: Success
          '404':
             description: No products in store
        """
        if productId:
            product = product_obj.fetch_product(productId)
            response = product
        
        else:
            products =  product_obj.fetchall_products()
            response = products
        return response

    def post(self):
        data = request.get_json()
        user_role = get_jwt_identity()
        jti = get_raw_jwt()['jti']
        print(jti)
        product_name = data.get("product_name")
        quantity = data.get("quantity")
        unit_cost = data.get("unit_cost")
        category = data.get("category")
        response = ""

        is_revoked = check_item_exists('token_jti', 'blacklisted', jti, cursor )

        if is_revoked:
            return jsonify({'msg': 'token already revoked'}), 401

        if user_role['user_role'] == 'admin':
            response = product_obj.add_product(product_name, category, quantity, unit_cost) 
            response = response           
        else:
            response = {'error': 'Only admins can add a product'}
            response = jsonify(response), 401
        return response

    def put(self, productId):
        response = None
        user_role = get_jwt_identity()
        jti_value = get_raw_jwt()['jti']

        token_revoked = check_item_exists('token_jti', 'blacklisted', jti_value, cursor )

        if token_revoked:
            return jsonify({'msg': 'token already revoked'}), 401


        if user_role['user_role'] == 'admin':
            response = product_obj.change_product_details(productId)
            response = response

        else:
            response = {'mesage': 'Only admins can edit a product.'}
            response = jsonify(response), 401
        return response

    def delete(self, productId):
        message  = None
        user_identity = get_jwt_identity()
        jti = get_raw_jwt()['jti']

        token_was_revoked = check_item_exists('token_jti', 'blacklisted', jti, cursor )

        if token_was_revoked:
            return jsonify({'msg': 'token already revoked'}), 401
        if user_identity['user_role'] == 'admin':
            message = product_obj.delete_product(productId)
        else:
            message = {'message':'Only admins can delete a product'}
            message = jsonify(message), 401
        return message

