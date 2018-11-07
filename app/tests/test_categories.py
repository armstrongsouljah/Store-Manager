from .base import BaseTestCase
import json


class TestCategories(BaseTestCase):

    category=dict(
        category_name ='detergents'
    )
    

    def test_admin_can_add_category(self):
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
                '/api/v2/categories',
                data=json.dumps(self.category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category has been successfully addded', res2.data)
    
    def test_category_cannot_be_blank(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}
            self.category['category_name'] = ''

            res2 = self.client.post(
                '/api/v2/categories',
                data=json.dumps(self.category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category cannot be blank', res2.data)
    
    def test_category_name_cannot_contain_spaces(self):
        with self.app.app_context():            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}
            self.category['category_name'] = 'detergents and more'

            res2 = self.client.post(
                '/api/v2/categories',
                data=json.dumps(self.category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category should only contain alphabetical characters.', res2.data)

    def test_category_name_must_be_a_string(self):
        with self.app.app_context():            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}
            self.category['category_name'] = 2018

            res2 = self.client.post(
                '/api/v2/categories',
                data=json.dumps(self.category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category name accepts string characters', res2.data)

    def test_prevent_attendant_from_adding_category(self):
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
                '/api/v2/categories',
                data=json.dumps(self.category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Only admin can add product categories', res2.data)

    def test_can_list_categories(self):
        with self.app.app_context():
            res2 = self.client.get(
                '/api/v2/categories',
                content_type='application/json'
            )
        self.assertTrue(res2.data)

    def test_can_fetch_a_single_categories(self):
        with self.app.app_context():
            res2 = self.client.get(
                '/api/v2/categories/1',
                content_type='application/json'
            )
        self.assertTrue(res2.data)
    

    def test_only_admin_can_add_update_category(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.non_admin),
                content_type='application/json'
            )
            new_category= dict(
                category_name='christmas'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.put(
                '/api/v2/categories/1',
                data=json.dumps(new_category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Only admin can edit product categories', res2.data)
    def test_can_add_update_category(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            new_category= dict(
                category_name='christmas'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.put(
                '/api/v2/categories/1',
                data=json.dumps(new_category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category updated successfully', res2.data)

    def test_can_only_update_existing_category(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            new_category= dict(
                category_name='christmas'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.put(
                '/api/v2/categories/5',
                data=json.dumps(new_category),
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category doesnot exis', res2.data)


    def test_only_admin_can_delete_category(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.non_admin),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.delete(
                '/api/v2/categories/5',
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Only admin can delete product categories', res2.data)
    
    def test_can_only_delete_existing_category(self):
        with self.app.app_context():
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.delete(
                '/api/v2/categories/5',
                content_type='application/json',
                headers=headers
            )
        self.assertIn(b'Category doesnot exis', res2.data)
