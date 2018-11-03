from flask import jsonify
from databases.server import DatabaseConnection
from  app.utils import fetch_all

class SalesRecord:
    """ Class that provides for manipluation of sales data """

    def __init__(self):

        self.db = DatabaseConnection().cursor
    

    def make_sale_record(self, userId, productId, quantity):

        response = None

        product_query = f"""
            SELECT quantity, unit_cost from products
            WHERE product_id = {productId} """
        self.db.execute(product_query)
        returned_product = self.db.fetchone()

        if not userId or not productId or not quantity:
            response = {'error': 'Product, attendant, and quantity cannot be blank'}

        if not isinstance(productId, int) or not isinstance(quantity, int) \
                   or not isinstance(userId, int):
            response = {'error': 'Product/quantity and attendant must be numbers'}
        
        if returned_product is None:
            response = {'error':'Couldnot find the product.'}

        if returned_product is not None and quantity > returned_product['quantity']:
            response = {'error':'You are trying to sell more than what is in stock'}

        if returned_product and returned_product['quantity'] == 0:
            response = {'error': 'Product is out of stock'}
        
        if response:
            return jsonify(response), 400

        else:
            total_cost = (quantity * returned_product['unit_cost'])
            new_stock = returned_product['quantity']-quantity
            
            sale_query = f"""
             INSERT INTO sales (attendant,product_sold, quantity, total_cost)
             VALUES ({userId}, {productId}, {quantity}, {total_cost})
            """
            update_stock = f"""
            UPDATE products SET quantity={new_stock}
            WHERE product_id={productId}
            """
            self.db.execute(update_stock)
            self.db.execute(sale_query)

            response = jsonify({'message':'Sales record saved successfully'}), 201
        return response
    
    def get_sales_by_attendant(self, attendant_id):
        """ return sales made by an attendant """
        attendant_check = f"""
            SELECT * FROM sales WHERE attendant='{attendant_id}'
        """
        response = None
        self.db.execute(attendant_check)
        attendant_sales = self.db.fetchall()

        if attendant_sales:
            response = jsonify(attendant_sales), 200
        else:
            response = jsonify({'message': 'Could not find the sales for that attendant'}), 400
        return response

    def get_all_sales(self):
        return fetch_all('sales', self.db)
