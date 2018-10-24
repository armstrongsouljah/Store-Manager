import datetime

from flask import request

from app.utils import (get_collection, get_item_id, is_empty,
                       validate_entry, validate_sales_data)

class Sale:
    """ stores all the sales made in the store """
    def __init__(self):
        self.sales = []
    
    @property
    def get_all_sales(self):
        return get_collection(self.sales)

    def add_sale(self):
        data = request.get_json()
        amount = data.get("amount_made")
        products = data.get("products_sold")
        attendant = data.get("attendant_name")
        
        sale_record = dict(
            sale_id = get_item_id('sale_id', self.sales),
            attendant_name = attendant,
            products_sold = products,
            amount_made = amount,
            time_of_sale = datetime.datetime.utcnow()
        )

        sales_errors = validate_sales_data(products, amount, attendant)
        
        if sales_errors:
            return sales_errors

        self.sales.append(sale_record)
        message = {"msg":"Sale recorded successfully"}
        return message       

    def get_sale_by_id(self, sale_id):
        """ returns a single product based off the supplied id """
        sale_id = validate_entry(sale_id, int)
        message = None
        selected_sale = [record for record in self.sales if record["sale_id"] == sale_id]
        if is_empty(selected_sale):
            message = {"msg":"No record matching selection"}
            return message
        else:
            message = selected_sale[0]
        return message
