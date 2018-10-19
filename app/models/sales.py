import datetime

from flask import request

from app.utils import (get_id, validate_amount, validate_attendant,
                       validate_id, validate_products)


class Sale:
    """ stores all the sales made in the store """
    def __init__(self):
        self.sales = []
    
    def get_all_sales(self):
        if len(self.sales) == 0:
            message = {"message":"No sales records yet"}
            return message
        return self.sales

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
        return self.sales

    def check_sale_exists(self, id):
        sale = [item for item in self.sales if item["sale_id"]==id]
        if sale:
            message = sale
        else:
            message = {"msg":"sale not found"}
        return message          

    def get_sale_by_id(self, id):
        """ returns a single product based off the supplied id """
        id = validate_id(id)
        message = None
        if len(self.sales) == 0:
            message = {"msg":"No sales records"}, 404
        if len(self.sales) > 0:
            message = self.check_sale_exists(id)
        return message
