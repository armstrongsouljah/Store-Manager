from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from app.models.products import Product

product_obj = Product()


class ProductsView(MethodView):
    """ Enables the admin user to add a product to the store """

    def get(self, productId=None):
        if productId:
            response = product_obj.fetch_product(productId)
        else:
            response =  product_obj.fetchall_products()
        return jsonify(response)

    def post(self):
        data = request.get_json()
        user_role = get_jwt_identity()
        product_name = data.get("product_name")
        quantity = data.get("quantity")
        unit_cost = data.get("unit_cost")
        response = ""

        if user_role['user_role'] == 'admin':
            response = product_obj.add_product(product_name, quantity, unit_cost)
            
        else:
            response = {'msg': 'Only admins can add a product'}
        return jsonify(response)

    def put(self, productId):
        response = None
        user_role = get_jwt_identity()

        if user_role['user_role'] == 'admin':
            response = product_obj.change_product_quantity(productId)
        else:
            response = {'msg': 'Only admins can edit a product.'}
        return jsonify(response)

    def delete(self, productId):
        message  = None
        admin_role = get_jwt_identity()


        if admin_role['user_role'] == 'admin':
            message = product_obj.delete_product(productId)
        else:
            message = {'msg':'Only admins can delete a product'}
        return jsonify(message)

