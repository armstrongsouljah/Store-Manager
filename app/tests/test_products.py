from .base import BaseTestCase
import json


class TestProducts(BaseTestCase):

    product=dict(
        product_name='Soy sauce',
        quantity=34,
        unit_cost=15000
    )
    invalid_product = dict(
        product_name=454545,
        quantity=34,
        unit_cost=15000
    )

    def test_admin_can_add_product(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Product successfully added', res2.data)

    

    def test_invalid_product_name(self):
        with self.app.app_context():

            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/products',
                data=json.dumps(self.invalid_product),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Product name must be a string', res2.data)

    def test_invalid_product_quantity_or_unitcost(self):
        with self.app.app_context():
            self.invalid_product['product_name'] = 'Foil paper'
            self.invalid_product['quantity'] = 'Kampala'
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/products',
                data=json.dumps(self.invalid_product),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'quantity/unitcost must be intergers', res2.data)

    
    def test_product_quantity_or_unitcost_is_zero(self):
        with self.app.app_context():
            self.invalid_product['product_name'] = 'Foil paper'
            self.invalid_product['quantity'] = 0
            self.invalid_product['unit_cost'] = 0
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/products',
                data=json.dumps(self.invalid_product),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'quantity/unitcost must be above zero', res2.data)

    def test_only_admin_can_add_product(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.non_admin),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Only admins can add a product', res2.data)


    
    def test_admin_can_update_product_quantity(self):
        with self.app.app_context():
            update = {
                'quantity':56,
                'unit_cost':360000
            }
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )

            res2 = self.client.put(
                '/api/v2/products/2',
                data=json.dumps(update),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'product updated successfully', res2.data)

    
    def test_admin_can_delete_a_product(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/products',
                data=json.dumps(self.product),
                content_type='application/json',
                headers=headers
            )

            res2 = self.client.delete(
                '/api/v2/products/1',
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Product successfully deleted', res2.data)


    def test_can_fetch_a_product(self):
        res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
        data = json.loads(res.data)
        token=data.get('token')
        headers = {'Authorization': f'Bearer {token}'}

        self.client.post(
            '/api/v2/products',
            data=json.dumps(self.product),
            content_type='application/json',
            headers=headers
        )
        res2 = self.client.get(
            '/api/v2/products/2',
            content_type='application/json'
        )
        print(res.data)
        self.assertIn(b'Soy sauce', res2.data)
