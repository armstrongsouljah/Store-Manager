from flask import request
from databases.server import DatabaseConnection
from app.utils import validate_product_entries
class Product:
    """ Class for handling product operations in the store """

    def __init__(self,):
        self.db = DatabaseConnection().cursor
             
    
    def add_product(self, productname, quantity, unit_cost):
        message = None
        query = f"""
            INSERT INTO products(product_name, quantity, unit_cost)
            VALUES('{productname}', '{quantity}', '{unit_cost}')
        """

        message = validate_product_entries(productname, quantity, unit_cost)

        if message:
            return message

        try:
            self.db.execute(query)
            message = {'msg': 'Product successfully added'}
        except Exception as  E:
            message = {'msg': f'Query failed due to: {E}'}
        return message

    
    def change_product_quantity(self, productId):
        """ modifies product in the store """
        data = request.get_json()
        quantity = data.get('quantity')
        message = None
        updated_rows = 0
        
        update = f"""
           UPDATE products SET quantity ='{quantity}'
           WHERE product_id = '{productId}'
        """
        query = f"""
           SELECT product_name, quantity FROM products
                WHERE product_id ='{productId}'
        """

        self.db.execute(query)
        row = self.db.fetchone()
        
        if row is not None:
            try:
                self.db.execute(update)
                message = {'msg': 'product updated successfully'}
            except Exception as E:
                message = E
        else:
            message = {'msg':'product doesnot exist'}
        return message

        


        

        



