import json
import unittest

from flask import request
from flask_jwt_extended import JWTManager, create_access_token

from app import app, create_app_environment, jwt
from app.config import BaseConfig
from app.models.products import Product
from app.utils import bp, get_item_id


class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.app = create_app_environment('testing')
        self.app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY
        self.app.register_blueprint(bp, url_prefix='/api/v1')
        self.product_obj = Product()
        self.jwt = JWTManager(self.app)
        self.products  = self.product_obj.products
        self.client = self.app.test_client(self)
        self.product_uri = 'api/v1/products'
        self.sample_product = dict(
            product_id = get_item_id('product_id', self.product_obj.products),
            product_name = "Cooker",
            product_category="Electronics",
            quantity=37,
            unit_cost=13000000
        )

        self.empty_product = dict(
            product_name = "",
            product_category="",
            quantity=None,
            unit_cost=None
        )

    

    def test_admin_or_attendant_can_get_products(self):
        res = self.client.get(self.product_uri)
        self.assertEqual(200, res.status_code, msg="found product")

    def test_can_get_specific_product(self):
        id = 1
        
        res = self.client.get(
            'api/v1/products/%d' %id,
            content_type='application/json'
        )
        self.assertEqual(200, res.status_code, msg="found product")

    def test_cannot_get_non_existent_id(self):

        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
            res = self.client.get("api/v1/products/34")
            data = json.loads(res.data)
        # print(data)
        self.assertEqual("Item not found", data['msg'], msg="product not found")
       
    def test_admin_can_add_product(self): 
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
            self.assertEqual(200, res.status_code)

    def test_admin_can_add_valid_category(self):        
        with self.app.app_context():
            self.sample_product["product_category"] = 23233
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
        # print(res.data)
        # print(res.status_code)
        # self.product_obj.get_products()  
        self.assertEqual(500, res.status_code)

    def test_admin_can_add_valid_product_name(self):        
        with self.app.app_context():
            self.sample_product["product_name"] = 23233
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
        # print(res.data)
        # print(res.status_code)
        # self.product_obj.get_products()  
        self.assertEqual(500, res.status_code)
    
    def test_admin_can_add_valid_unitcost(self):        
        with self.app.app_context():
            self.sample_product["unit_cost"] = 'klk'
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
     
        self.assertEqual(500, res.status_code)

    def test_admin_can_add_valid_quantity(self):        
        with self.app.app_context():
            self.sample_product["quantity"] = 'jj'
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
        # print(res.data)
        # print(res.status_code) 
        self.assertEqual(500, res.status_code)
    


    def test_admin_dont_add_empty_product(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}   
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.empty_product)
            )
        self.assertEqual(500, res.status_code)
    
    # @unittest.skip('WIP')
    def test_admin_can_edit_product(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            data = {'unit_cost': 4000} 
            self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )

            update = self.client.put(
                '/api/v1/products/2',
                content_type='application/json',
                headers=headers,
                data= json.dumps(data)
            )
            data = json.loads(update.data)
        self.assertEqual(data.get("msg"), "Updated successfully")
        self.assertEqual(0, len(self.product_obj.products))

    def test_admin_can_delete_product(self):
        with self.app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}   
            self.test_admin_can_add_product()
            delete = self.client.delete(
                '/api/v1/products/1',
                content_type='application/json',
                headers=headers,
            )
            data = json.loads(delete.data)
        self.assertEqual(data.get("msg"), "Item removed successfully")
        # self.assertEqual(0, len(self.product_obj.products))
        # self.assertEqual(201, delete.status_code)

        
        
    
    # def tearDown(self):
    #     self.app = None
    #     self.product_obj = None
    #     self.client = None
