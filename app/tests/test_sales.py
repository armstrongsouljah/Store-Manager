import json
from .base import BaseTestCase


class TestSales(BaseTestCase):
    product=dict(
        product_name='Soy sauce',
        quantity=34,
        unit_cost=15000
    )
    
    def test_get_all_sales(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user)
            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}
        
            res2  = self.client.get(
                '/api/v2/sales',
                headers = headers,
                content_type='application/json'
            )
            print(res2.data)
        self.assertIn(b'No records in store', res2.data)

    def test_only_attendant_can_make_a_sale(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user)

            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )
        
            res2  = self.client.post(
                '/api/v2/sales',
                headers = headers,
                content_type='application/json',
                data = json.dumps(self.sale_data)
            )
        self.assertIn(b'Only attendants can make a sale', res2.data)

    def test_can_make_a_sale(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.non_admin)

            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )
        
            res2  = self.client.post(
                '/api/v2/sales',
                headers = headers,
                content_type='application/json',
                data = json.dumps(self.sale_data)
            )
        self.assertIn(b'Sales record saved successfully', res2.data)
    


    def test_for_invalid_sale_quantity(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.non_admin)

            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )

            self.sale_data['quantity'] = '#234'
        
            res2  = self.client.post(
                '/api/v2/sales',
                headers = headers,
                content_type='application/json',
                data = json.dumps(self.sale_data)
            )
        self.assertIn(b'Invalid input for stock or product', res2.data)

    def test_for_negative_sale_stock(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.non_admin)

            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )

            self.sale_data['quantity'] = 0
        
            res2  = self.client.post(
                '/api/v2/sales',
                headers = headers,
                content_type='application/json',
                data = json.dumps(self.sale_data)
            )
        self.assertIn(b'Product or quantity cannot be empty', res2.data)

    
    def test_only_admin_can_filter_sales_by_existing_only_existing_attendants(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.user)
            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}
        
            res2  = self.client.get(
                '/api/v2/sales/5',
                headers = headers,
                content_type='application/json'
            )
        self.assertIn(b'Could not find the sales for that attendant', res2.data)
    
    def test_only_admin_can_fetch_all_sales(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                content_type='application/json',
                data=json.dumps(self.non_admin)
            )
            data = json.loads(res.data)

            token = data['token']
            headers = {'Authorization': f'Bearer {token}'}
        
            res2  = self.client.get(
                '/api/v2/sales',
                headers = headers,
                content_type='application/json'
            )
        self.assertTrue(res2.data)
           
