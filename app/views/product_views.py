from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from app.models.products import Product

product_obj = Product()

class ProductsListView(MethodView):
    pass

class ProductOperationsView(MethodView):
    """ Enables the admin user to add a product to the store """

    def post(self):
        data = request.get_json()
        admin_status = get_jwt_identity()
        product_name = data.get("product_name")
        quantity = data.get("quantity")
        unit_cost = data.get("unit_cost")
        response = ""

        if admin_status == True:
            response = product_obj.add_product(product_name, quantity, unit_cost)
            
        else:
            response = {'msg': 'Only admins can add a product'}
        return jsonify(response)
        
