from flask import request, jsonify

from app.utils import validate_product_change_details, validate_product_entries, check_item_exists
from databases.server import DatabaseConnection


class Product:
    """ Class for handling product operations in the store """

    def __init__(self,):
        self.database_cursor = DatabaseConnection().cursor

    def fetch_product(self, productId):
        response = None
        product_query = f"""
             SELECT product_name, quantity, unit_cost FROM
             products WHERE product_id='{productId}'
        """
        self.database_cursor.execute(product_query)
        returned_product = self.database_cursor.fetchone()

        if not isinstance(productId, int):
            response = jsonify({"error": "Product id must be an integer"}), 400
            return response
        
        
        if returned_product is not None:
            response = jsonify({"returned_product": returned_product}), 200
        else:
            response =  jsonify({"message":"product not found"}), 404
        return response

    def fetchall_products(self):
        response = None
        products_query = """
           SELECT * FROM products
        """
        self.database_cursor.execute(products_query)
        query_result = self.database_cursor.fetchall()
        if query_result:
            response =  jsonify({"products":query_result}), 200
        else:
            response = jsonify({'message': 'No products in store'}), 404
        return response
              
             
    def add_product(self, productname, category,  quantity, unit_cost):
        message = None
        insert_product_query = f"""
            INSERT INTO products(product_name, category, quantity, unit_cost)
            VALUES('{productname}', '{category}', '{quantity}', '{unit_cost}')
        """
        existing_product = check_item_exists('product_name', 'products', productname, self.database_cursor)

        product_errors = validate_product_entries(productname, category, quantity, unit_cost)

        if product_errors:
            message = product_errors

        if existing_product:
            message = jsonify({'message': 'product already exists'}), 400

        if message:
           return message

        else:
            try:
                self.database_cursor.execute(insert_product_query)
                message = jsonify({'message': 'Product successfully added'}), 201
            except Exception as  E:
                message = jsonify({'message': f'Query failed due to: {E}'}), 500
        return message

    
    def change_product_details(self, productId):
        """ modifies product in the store """
        change_product_data = request.get_json()
        quantity = change_product_data.get('quantity')
        unit_cost = change_product_data.get('unit_cost')
        message = None
        validate_product_detail = validate_product_change_details(quantity, unit_cost)        
        product_update_query = f"""
           UPDATE products SET quantity ='{quantity}',
           unit_cost='{unit_cost}'
           WHERE product_id = '{productId}'
        """
        check_product_exists_query = f"""
           SELECT product_name, quantity FROM products
                WHERE product_id ='{productId}'
        """
        if validate_product_detail:
            return jsonify(validate_product_detail), 400

        self.database_cursor.execute(check_product_exists_query)
        product_exists = self.database_cursor.fetchone()
        
        if product_exists:
            try:
                self.database_cursor.execute(product_update_query)
                message = jsonify({'message': 'product updated successfully'}), 200
            except Exception as error:
                message = {'message': error}
        else:
            message = jsonify({'message':'product doesnot exist'}), 400
        return message
    
    def delete_product(self, productId):
        response = None
        product_to_delete_query =  f"""
           SELECT product_name, quantity FROM products
                WHERE product_id ='{productId}'
        """
        delete_existing_product_query = f"""
                DELETE FROM products WHERE product_id='{productId}'
        """
        # get  an item the delete the fetched item
        self.database_cursor.execute(product_to_delete_query)
        product_to_delete = self.database_cursor.fetchone()

        if product_to_delete is not None:
            try:
                self.database_cursor.execute(delete_existing_product_query)
                response = jsonify({'message': 'Product successfully deleted'}), 202
            except Exception as error:
                response = {'message': error}
        else:
            response = jsonify({'message': 'product does not exist'}), 404
        return response
