from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from app.models.sales import SalesRecord



sale_obj = SalesRecord()


class SalesView(MethodView):
    def post(self):
        response = None
        sale_data = request.get_json()
        user_identity = get_jwt_identity()
        attendant = user_identity['user_id']
        product_sold = sale_data.get("product_sold")
        quantity = sale_data.get("quantity")

        if user_identity['user_role'] != 'attendant' :
            response = {'msg':'Only attendants can make a sale'}
        else:
            response = sale_obj.make_sale_record(attendant, product_sold, quantity)
        return jsonify(response)

    def get(self, attendant_id=None):
        """ Collects sales for all attendants or a single attendant """
        response = None

        logged_in_user = get_jwt_identity()

        if logged_in_user['user_role']=='admin':
            response = sale_obj.get_all_sales()

        if logged_in_user['user_role']=='admin' and attendant_id:
            response = sale_obj.get_sales_by_attendant(attendant_id)

        if logged_in_user['user_role'] == 'attendant':
            response = {'message': 'You have no access to this resource'}
        return jsonify(response)
        
        