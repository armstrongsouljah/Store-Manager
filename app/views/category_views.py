from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from app.models.categories import Category

category_obj = Category()


class CategoryViews(MethodView):
    """ handles all operations regarding """

    def post(self):
        category_data =  request.get_json()
        user_identity = get_jwt_identity()
        categoryname = category_data.get("category_name")
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
        
        if user_identity.get('user_role') == 'admin':
            response = category_obj.change_category_name(categoryId, categoryname)
        else:
            response = jsonify({'message': 'Only admin can edit product categories'}), 401
        return response 
    
    def delete(self, categoryId):
        user_identity = get_jwt_identity()
        if user_identity.get('user_role') == 'admin':
            response = category_obj.remove_category(categoryId)
        else:
            response = jsonify({'message': 'Only admin can delete product categories'}), 401
        return response 

