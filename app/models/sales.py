import datetime

from flask import request

from app.utils import (check_exists, get_id, get_collection, validate_amount, validate_attendant,
                       validate_id, validate_products)


class Sale:
    """ stores all the sales made in the store """
    def __init__(self):
        self.sales = []
    
    @property
    def get_all_sales(self):
        return get_collection(self.sales)

    def add_sale(self):
        data = request.get_json()
        amount = validate_amount(data.get("amount_made"))
        products = validate_products(data.get("products_sold"))
        attendant = validate_attendant(data.get("attendant_name"))
        
        sale_record = dict(
            sale_id = get_id(self.sales),
            attendant_name = attendant,
            products_sold = products,
            amount_made = amount,
            time_of_sale = datetime.datetime.utcnow()
        )
        if sale_record in self.sales:
            message = {"msg":"sale record already added"}
            return  message, 400
        self.sales.append(sale_record)
        message = {"msg":"Sale recorded successfully"}
        return message       

    def get_sale_by_id(self, id):
        """ returns a single product based off the supplied id """
        id = validate_id(id)
        message = None
        if len(self.sales) == 0:
            message = {"msg":"No sales records"}
        if len(self.sales) > 0:
            message = check_exists("sale_id", self.sales, id)
        return message
