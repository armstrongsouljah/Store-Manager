from flask import request
from databases.server import DatabaseConnection
from app.utils import validate_product_entries
class Product:
    """ Class for handling product operations in the store """

    def __init__(self,):
        self.db = DatabaseConnection().cursor

    def fetch_product(self, productId):
        response = None
        product_query = f"""
             SELECT product_name, quantity, unit_cost FROM
             products WHERE product_id='{productId}'
        """
        self.db.execute(product_query)
        result = self.db.fetchone()

        if not isinstance(productId, int):
            response = {"error": "Product id must be an integer"}
            return response
        
        
        if result is not None:
            response = {"msg": result}
        else:
            response =  {"msg":"product not found"}
        return response

    def fetchall_products(self):
        response = None
        products_query = """
           SELECT * FROM products
        """
        self.db.execute(products_query)
        query_result = self.db.fetchall()
        if query_result:
            response =  query_result
        else:
            response = {'message': 'No products in store'}
        return response
              
             
    def add_product(self, productname, quantity, unit_cost):
        message = None
        query = f"""
            INSERT INTO products(product_name, quantity, unit_cost)
            VALUES('{productname}', '{quantity}', '{unit_cost}')
        """
        existing_query = f"""
            SELECT product_name FROM products
            WHERE product_name='{productname}'
        """
        self.db.execute(existing_query)
        row = self.db.fetchone()

        message = validate_product_entries(productname, quantity, unit_cost)

        if message:
            return message

        if row is not None:
            message = {'error': 'product already exists'}
        else:
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
                message = {'msg': E}
        else:
            message = {'msg':'product doesnot exist'}
        return message
    
    def delete_product(self, productId):
        response = None
        sql =  f"""
           SELECT product_name, quantity FROM products
                WHERE product_id ='{productId}'
        """
        del_sql = f"""
                DELETE FROM products WHERE product_id='{productId}'
        """
        # get  an item the delete the fetched item
        self.db.execute(sql)
        result = self.db.fetchone()

        if result is not None:
            try:
                self.db.execute(del_sql)
                response = {'msg': 'Product successfully deleted'}
            except Exception as E:
                response = {'msg': E}
        else:
            response = {'msg': 'product does not exist'}
        return response


        


        

        



