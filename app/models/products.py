from databases.server import DatabaseConnection
class Product:
    """ Class for handling product operations in the store """

    def __init__(self,):
        self.db = DatabaseConnection().cursor
             
    
    def add_product(self, productname, quantity, unit_cost):
        message = None
        query = f"""
            INSERT INTO products(product_name, quantity, unit_cost)
            VALUES('{productname}', '{quantity}', '{unit_cost}')
            ON CONFLICT DO NOTHING; 
        """

        if not productname or not unit_cost or not quantity:
            message = {'msg': "productname/ unitcost or quantity can't be blank"}

        if productname =="" or productname ==" ":
            message = {'msg': 'Product cannot be an empty space'}

        if not isinstance(productname, str):
            message = {'msg':'Product name must be a string'}

        if not isinstance(quantity, int) or not isinstance(unit_cost, int):
            message = {'msg': 'quantity/unitcost must be intergers'}  

        if isinstance(quantity, int) and quantity < 1 \
        or isinstance(unit_cost, int) and unit_cost < 1:
            message = {'msg':'quantity/unitcost must be above zero'}
        if message:
            return message

        try:
            self.db.execute(query)
            message = {'msg': 'Product successfully added'}
        except Exception as  E:
            message = {'msg': f'Query failed due to: {E}'}
        return message

        

        



