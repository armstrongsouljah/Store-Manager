from app.api import bp
from flask import request, jsonify


@bp.route('/sales', methods=['GET'])
def get_sales():
    return jsonify({"message":"hello sales"})


@bp.route('/sales/<int:sales_id>')
def get_sale(sales_id):
    pass


@bp.route('/sales/add', methods =['POST'])
def add_sale():
    pass
