from flask import jsonify
from databases.server import DatabaseConnection
from app.utils import check_item_exists, validate_category_name, fetch_all, fetch_details_by_id, remove_entry_by_id



class Category:
    """ model for product categories """
    def __init__(self):
        self.db_cursor = DatabaseConnection().cursor

    def add_category(self, category_name):
        response = None
        insert_category_query = f"""
        INSERT INTO categories(category_name)
        VALUES ('{category_name}')
        """
        check_category_already_exists = check_item_exists('category_name', 'categories', category_name, self.db_cursor)

        category_has_errors = validate_category_name(category_name)

        if category_has_errors:
            response = category_has_errors

        if check_category_already_exists:
            response = {"message": "Category has already been added"}

        if response:
            return jsonify(response), 400   

        if not category_has_errors:
            try:
                self.db_cursor.execute(insert_category_query)
                response = jsonify({'message': 'Category has been successfully addded'}), 201
            except Exception as error:
                response = jsonify({'message': f'query failed due to {error}'}), 400
        return response

    def retrieve_all_categories(self):
        response  = fetch_all('categories', self.db_cursor)
        return response

    def retrieve_category_by_id(self, categoryId):
        response = fetch_details_by_id('category_id',categoryId,'categories', self.db_cursor)
        return response

    def change_category_name(self, categoryId, categoryname):
        response = None
        category_change_query = f"""
        UPDATE categories SET category_name='{categoryname}'
        """
        category_errors = validate_category_name(categoryname)
        category_exists = check_item_exists('category_id', 'categories', categoryId, self.db_cursor)
        if category_errors:
            response = category_errors        

        if not category_exists:
            response = jsonify({'message': 'Category doesnot exist'}), 404
        
        if response:
            return response        

        try:
            self.db_cursor.execute(category_change_query)
            response = jsonify({'message': 'Category updated successfully'}), 202
        except Exception as error:
            response = jsonify({'message': f'Query failed due to {error}'}), 400
        return response
        

    def remove_category(self, categoryId):
        response = None
        
        category_exists = check_item_exists('category_id', 'categories', categoryId, self.db_cursor)

        if not category_exists:
            response = jsonify({'message': 'Category doesnot exist'}), 404
            return response
        else:
            response = remove_entry_by_id('category_id', 'categories', categoryId, self.db_cursor)
        return response

    def was_token_revoked(self, token_jti):
        token_revoked_query = f"""
        SELECT token_jti FROM blacklisted 
        WHERE token_jti='{token_jti}'
        """
        self.db_cursor.execute(token_revoked_query)
        returned_token = self.db_cursor.fetchone()

        if returned_token:
            return True
        return False
