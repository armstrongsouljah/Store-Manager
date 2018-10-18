
from flask import request, jsonify
from app.models.sales import Sale
from app.utils import bp, jwt
from flask_jwt_extended import get_jwt_identity, jwt_required


sales_obj = Sale()

@bp.route('/sales', methods=['GET'])
@jwt_required
def get_sales():
    user = get_jwt_identity()
    if user == 'admin':
        response = sales_obj.get_all_sales()
        return jsonify(response)
    return jsonify(message="Access denied"), 401


@bp.route('/sales/<int:sales_id>')
def get_sale(sales_id):
    pass


@bp.route('/sales', methods =['POST'])
@jwt_required
def add_sale():
    current_user  = get_jwt_identity()
    if current_user == 'attendant':
        response = sales_obj.add_sale()
        return jsonify(response), 200
    return jsonify({"message":"Access only for attendants"}), 401
