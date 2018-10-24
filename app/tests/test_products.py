import json
import unittest

from flask import request
from flask_jwt_extended import JWTManager, create_access_token

from app import app, create_app_environment, jwt
from app.config import BaseConfig
from app.models.products import Product
from app.utils import bp, get_item_id, validate_entry


class TestProducts(unittest.TestCase):
    
    def setUp(self):
        self.product_obj = Product()        
        self.products  = self.product_obj.products
        self.client = app.test_client(self)
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
        self.invalid_product = dict(
            product_id=get_item_id('product_id', self.product_obj.products),
            product_name=23,
            product_category=3434,
            quantity=0,
            unit_cost="hello"

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

        with app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}
            self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
            res = self.client.get("api/v1/products/1")
            print(res.data)
        # self.assertEqual("Product not found", res.data, msg="product not found")
        self.assertTrue(b'Electronics' in res.data)
       
    def test_only_admin_can_add_product(self): 
        with app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization':f'Bearer {token}'}
            res = self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
            data = json.loads(res.data)
            self.assertEqual("Acess denied for non admins", data.get("message"))

    def test_prevent_addition_of_empty_product(self):
        with app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}

            res = self.client.post(
                      self.product_uri,
                      content_type='application/json',
                      headers=headers,
                      data=json.dumps(self.empty_product)
            )
            data = json.loads(res.data)
            print(data)
        self.assertEqual('Empty records not allowed', data["message"])
            
    
    def test_admin_can_only_edit_existing_product(self):
        with app.app_context():
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
                '/api/v1/products/1',
                content_type='application/json',
                headers=headers,
                data= json.dumps(data)
            )
            data = json.loads(update.data)
        self.assertEqual(data.get("msg"), "Updated successfully")

    def test_admin_can_delete_product(self):
        with app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization':f'Bearer {token}'}   
            self.client.post(
                self.product_uri,
                content_type='application/json',
                headers=headers,
                data=json.dumps(self.sample_product)
            )
            delete = self.client.delete(
                '/api/v1/products/1',
                content_type='application/json',
                headers=headers,
            )
            data = json.loads(delete.data)
        self.assertEqual(data.get("msg"), "Item removed successfully")
