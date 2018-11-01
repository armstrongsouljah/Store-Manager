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
        q_result = self.db.fetchone()

        if not userId or not productId or not quantity:
            response = {'error': 'Product, attendant, and quantity cannot be blank'}

        if not isinstance(productId, int) or not isinstance(quantity, int) \
                   or not isinstance(userId, int):
            response = {'error': 'Product/quantity and attendant must be numbers'}
        
        if q_result is None:
            response = {'error':'Couldnot find the product.'}

        if q_result is not None and quantity > q_result['quantity']:
            response = {'error':'You are trying to sell more than what is in stock'}

        if q_result and q_result['quantity'] == 0:
            response = {'error': 'Product is out of stock'}
        
        if response:
            return response

        else:
            total_cost = (quantity * q_result['unit_cost'])
            new_stock = q_result['quantity']-quantity
            
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

            response = {'msg':'Sales record saved successfully'}
        return response
    
    def get_sales_by_attendant(self, attendant_id):
        """ return sales made by an attendant """
        attendant_check = f"""
            SELECT * FROM sales WHERE attendant='{attendant_id}'
        """
        query_response = None
        self.db.execute(attendant_check)
        query_result = self.db.fetchall()

        if query_result:
            query_response = query_result
        else:
            query_response = {'error': 'Could not find the sales for that attendant'}
        return query_response

    def get_all_sales(self):
        return fetch_all('sales', self.db)
