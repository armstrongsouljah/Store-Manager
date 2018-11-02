from flask import request

from app.utils import validate_product_change_details, validate_product_entries
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
            response = {"error": "Product id must be an integer"}
            return response
        
        
        if returned_product is not None:
            response = {"returned_product": returned_product}
        else:
            response =  {"message":"product not found"}
        return response

    def fetchall_products(self):
        response = None
        products_query = """
           SELECT * FROM products
        """
        self.database_cursor.execute(products_query)
        query_result = self.database_cursor.fetchall()
        if query_result:
            response =  query_result
        else:
            response = {'message': 'No products in store'}
        return response
              
             
    def add_product(self, productname, quantity, unit_cost):
        message = None
        insert_product_query = f"""
            INSERT INTO products(product_name, quantity, unit_cost)
            VALUES('{productname}', '{quantity}', '{unit_cost}')
        """
        existing_product_query = f"""
            SELECT product_name FROM products
            WHERE product_name='{productname}'
        """
        self.database_cursor.execute(existing_product_query)
        existing_product = self.database_cursor.fetchone()

        valid_product = validate_product_entries(productname, quantity, unit_cost)

        if valid_product:
            return valid_product

        if existing_product is not None:
            message = {'message': 'product already exists'}
        else:
            try:
                self.database_cursor.execute(insert_product_query)
                message = {'message': 'Product successfully added'}
            except Exception as  E:
                message = {'message': f'Query failed due to: {E}'}
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
            return validate_product_detail

        self.database_cursor.execute(check_product_exists_query)
        product_exists = self.database_cursor.fetchone()
        
        if product_exists:
            try:
                self.database_cursor.execute(product_update_query)
                message = {'message': 'product updated successfully'}
            except Exception as error:
                message = {'message': error}
        else:
            message = {'message':'product doesnot exist'}
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
                response = {'message': 'Product successfully deleted'}
            except Exception as error:
                response = {'message': error}
        else:
            response = {'message': 'product does not exist'}
        return response
