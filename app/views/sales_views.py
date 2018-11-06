from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from app.models.sales import SalesRecord
from app.utils import validate_sale_record


sale_obj = SalesRecord()


class SalesView(MethodView):
    
    def post(self):
        response = None
        sale_data = request.get_json()
        user_identity = get_jwt_identity()
        attendant = user_identity['user_id']
        product_sold = sale_data.get("product_sold")
        quantity = sale_data.get("quantity")

        validation_response = validate_sale_record(product_sold, quantity) 

        if user_identity['user_role'] != 'attendant' :
            return jsonify({'message':'Only attendants can make a sale'}), 401

        if validation_response:
            return validation_response
        else:
            response = sale_obj.make_sale_record(attendant, product_sold, quantity)
        return response

    def get(self, attendant_id=None):
        """ Collects sales for all attendants or a single attendant """
        response = None

        user_identity = get_jwt_identity()

        if user_identity['user_role']=='admin':
            sales  = sale_obj.get_all_sales()
            response = sales

        if user_identity['user_role']=='admin' and attendant_id:
            sales = sale_obj.get_sales_by_attendant(attendant_id)
            response = sales

        if user_identity['user_role'] == 'attendant':
            attendant_id = user_identity['user_id']
            response = sale_obj.get_sales_by_attendant(attendant_id)
        return response
        
        