import json
import unittest

from flask_jwt_extended import create_access_token, JWTManager

from app import app, create_app_environment, jwt
from app.config import BaseConfig
from app.models.sales import Sale
from app.utils import bp, get_id

class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app = create_app_environment('testing')
        self.app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY
        self.app.register_blueprint(bp, url_prefix='/api/v1')
        self.jwt = JWTManager(self.app)
        self.client = self.app.test_client(self)
        self.sales_uri = 'api/v1/sales'
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
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.get(
                self.sales_uri,
                headers=headers,
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(200, res.status_code)

    def test_attendant_not_allowed_to_get_sales(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.get(
                self.sales_uri,
                headers=headers,
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(401, res.status_code)

    
    def test_only_attendant_makes_sale(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                self.sales_uri,
                headers=headers,
                data=json.dumps(self.sale_record),
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(200, res.status_code)

    def test_for_empty_records(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                self.sales_uri,
                headers=headers,
                data=json.dumps(self.empty_record),
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(500, res.status_code)

    def test_for_valid_attendant_name(self):
        with self.app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            self.sale_record['attendant_name'] = 24888888
            res = self.client.post(
                self.sales_uri,
                headers=headers,
                data=json.dumps(self.sale_record),
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(500, res.status_code)



    
    def test_admin_doesnot_make_sale(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                self.sales_uri,
                headers=headers,
                data=json.dumps(self.sale_record),
                content_type='application/json'
            )
            print(res.status)
            self.assertEqual(401, res.status_code)

    def test_admin_attendant_get_sale_by_id(self):
        id = 7        
        res  = self.client.get(
             '/api/v1/sales/%d' %id,
             content_type='application/json'
        )
        print(res.data)
        data = json.loads(res.data)
        self.assertEqual("No sales records", data.get("msg"))
    