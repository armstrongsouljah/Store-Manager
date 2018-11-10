from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, get_raw_jwt
from app.models.categories import Category
from app.utils import check_item_exists
from databases.server import DatabaseConnection

category_obj = Category()
db_cursor = DatabaseConnection().cursor

class CategoryViews(MethodView):
    """ handles all operations regarding """

    def post(self):
        category_data =  request.get_json()
        user_identity = get_jwt_identity()
        categoryname = category_data.get("category_name")
        jti = get_raw_jwt()['jti']

        token_already_revoked = check_item_exists('token_jti', 'blacklisted', jti, db_cursor )

        if token_already_revoked:
            return jsonify({'msg': 'token already revoked'}), 401
        
        if user_identity.get('user_role') == 'admin':
            response = category_obj.add_category(categoryname)
        else:
            response = jsonify({'message': 'Only admin can add product categories'}), 401
        return response 

    def get(self, categoryId=None):
        if not categoryId:
            response = category_obj.retrieve_all_categories()
        else:
            response = category_obj.retrieve_category_by_id(categoryId)
        return response
    
    def put(self, categoryId):
        user_identity = get_jwt_identity()
        category_data = request.get_json()
        categoryname = category_data.get("category_name")

        jti = get_raw_jwt()['jti']

        token_already_revoked = check_item_exists('token_jti', 'blacklisted', jti, db_cursor )

        if token_already_revoked:
            return jsonify({'msg': 'token already revoked'}), 401
        
        if user_identity.get('user_role') == 'admin':
            response = category_obj.change_category_name(categoryId, categoryname)
        else:
            response = jsonify({'message': 'Only admin can edit product categories'}), 401
        return response 
    
    def delete(self, categoryId):
        user_identity = get_jwt_identity()

        jti = get_raw_jwt()['jti']

        token_already_revoked = check_item_exists('token_jti', 'blacklisted', jti, db_cursor )

        if token_already_revoked:
            return jsonify({'msg': 'token already revoked'}), 401
        if user_identity.get('user_role') == 'admin':
            response = category_obj.remove_category(categoryId)
        else:
            response = jsonify({'message': 'Only admin can delete product categories'}), 401
        return response 

