
from flask import request, jsonify
from flask.views import MethodView
from app.models.sales import Sale
from app.utils import bp
from flask_jwt_extended import get_jwt_identity, jwt_optional, jwt_required

sale_obj = Sale()

class Sales(MethodView):
    def __init__(self):
        self.obj = Sale()
        self.current_user = get_jwt_identity()

    def get(self, saleId=None):
        if saleId:
            message = sale_obj.get_sale_by_id(saleId)
            return jsonify(message)

        if not saleId and self.current_user != 'admin':
            message = {'message':'Only admins can view sales records'}

        else:
            message = sale_obj.get_all_sales
        return jsonify(message)

    def post(self):
        if self.current_user !='attendant':
            message = jsonify({'message':'Access only for attendants'})
            return message
        else:
            message = sale_obj.add_sale()
        return jsonify(message)
