import json
import unittest

from flask_jwt_extended import create_access_token, JWTManager

from app import app, create_app_environment, jwt
from app.config import BaseConfig
from app.models.sales import Sale
from app.views.salesviews import Sales
from app.utils import bp, get_id

class TestSales(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.obj =  Sale()
        self.sale_record = dict(
            sale_id = get_id(self.obj.sales),
            attendant_name = "Mwesigye",
            products_sold = [{"milk":12000}, {"chicken":18000}],
            amount_made = 30000,
            time_of_sale = "23, 9, 2018"
        )
        self.empty_record = dict(
            sale_id = get_id(self.obj.sales),
            attendant_name = None,
            products_sold = None,
            amount_made = None,
            time_of_sale = None
        )

    def test_admin_can_get_sales(self):
        with app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            link = 'http://localhost:5400/api/v1/sales'
            res = self.client.get(
                link,
                headers=headers,
                content_type='application/json'
            )
            self.assertEqual(200, res.status_code, msg="Returned sales records.")

    def test_attendant_not_allowed_to_get_sales(self):
        with app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.get(
                '/api/v1/sales',
                headers=headers,
                content_type='application/json'
            )
            data = json.loads(res.data)
            self.assertEqual("Only admins can view sales records", data.get("message"))

    
    def test_only_attendant_makes_sale(self):
        with app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                '/api/v1/sales',
                headers=headers,
                data=json.dumps(self.sale_record),
                content_type='application/json'
            )
            data = json.loads(res.data)
            self.assertEqual("Sale recorded successfully", data.get("msg"))
    
    def test_for_empty_records(self):
        with app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                '/api/v1/sales',
                headers=headers,
                data=json.dumps(self.empty_record),
                content_type='application/json'
            )
            data = json.loads(res.data)
            self.assertEqual('Not allowed to add empty values', data['error'])
    
    def test_for_invalid_products_sold(self):
        with app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            self.sale_record['attendant_name'] = 24888888
            self.sale_record['products_sold'] = 24888888
            self.sale_record['amount_made'] = 45660
            res = self.client.post(
                '/api/v1/sales',
                headers=headers,
                data=json.dumps(self.sale_record),
                content_type='application/json'
            )
            data = json.loads(res.data)
            self.assertEqual('Items must be a collection', data['error'])

    def test_admin_doesnot_make_sale(self):
        with app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                '/api/v1/sales',
                headers=headers,
                data=json.dumps(self.sale_record),
                content_type='application/json'
            )
            data = json.loads(res.data)
            self.assertEqual("Access only for attendants", data.get("message"))

    def test_admin_attendant_get_existing_sale_by_id(self):
        id = 7        
        res  = self.client.get(
             '/api/v1/sales/%d' %id,
             content_type='application/json'
        )
        print(res.data)
        data = json.loads(res.data)
        self.assertEqual("No record matching selection", data.get("msg"))
    