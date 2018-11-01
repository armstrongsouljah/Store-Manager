import json
from .base import BaseTestCase



class TestSales(BaseTestCase):
    
    def test_only_admin_can_get_all_sales(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v1/auth/login',
                content_type='application/json',
                data=json.dumps(self.non_admin)
            )
            data = json.loads(res.data)

            token = data['msg']
            headers = {'Authorization': f'Bearer {token}'}
        
            res2  = self.client.get(
                '/api/v1/sales',
                headers = headers,
                content_type='application/json'
            )
        self.assertIn(b'You have no access to this resource', res2.data)

    def test_only_attendant_can_make_a_sale(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v1/auth/login',
                content_type='application/json',
                data=json.dumps(self.user)

            )
            data = json.loads(res.data)

            token = data['msg']
            headers = {'Authorization': f'Bearer {token}'}
        
            res2  = self.client.post(
                '/api/v1/sales',
                headers = headers,
                content_type='application/json',
                data = json.dumps(self.sale_data)
            )
        self.assertIn(b'Only attendants can make a sale', res2.data)

    
    def test_only_can_filter_sales_by_existing_only_existing_attendants(self):
        with self.app.app_context():
            res = self.client.post(
                '/api/v1/auth/login',
                content_type='application/json',
                data=json.dumps(self.user)
            )
            data = json.loads(res.data)

            token = data['msg']
            headers = {'Authorization': f'Bearer {token}'}
        
            res2  = self.client.get(
                '/api/v1/sales/12',
                headers = headers,
                content_type='application/json'
            )
        self.assertIn(b'Could not find the sales for that attendant', res2.data)
           
