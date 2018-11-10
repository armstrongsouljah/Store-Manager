import json
from .base import BaseTestCase


class TestUsers(BaseTestCase):

    def test_userlogin(self):

        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
        self.assertIn(b'Logged in successfully', res.data)
    
    def test_invalid_details(self):
        self.user['username'] = ""
        with self.app.app_context():
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
        self.assertIn(b'invalid username/password try again', res.data)

    def test_user_signup(self):
        # only admins can register users
        
        with self.app.app_context():
            user_toregister = dict(
            username='wonderland',
            password='testing123',
            role='admin'
        )
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(user_toregister),
                content_type='application/json',
                headers=headers

            )
            response = json.loads(res2.data)
        self.assertEqual('Successfully registered', response.get('message'))

   
    def test_user_prevent_user_signs_up_more_than_one(self):
        # only admins can register users
        
        with self.app.app_context():
            user_toregister = dict(
            username='wonderland',
            password='testing123',
            role='admin'
        )
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(user_toregister),
                content_type='application/json',
                headers=headers

            )
            res3 = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(user_toregister),
                content_type='application/json',
                headers=headers

            )
            response = json.loads(res3.data)
        self.assertEqual('Username already taken', response.get('message'))




    def test_only_admin_can_add_user(self):
        with self.app.app_context():
            user_toregister = dict(
            username='livingstone',
            password='testing123',

            )
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.non_admin),
                content_type='application/json'
            )
            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}
            res2 = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(user_toregister),
                content_type='application/json',
                headers=headers

            )
            response = json.loads(res2.data)
        self.assertEqual('Access only for admins', response.get('message'))

    def test_prevent_revoked_token_from_accessing_protected_resource(self):
        with self.app.app_context():
            user_toregister = dict(
            username='livingstone',
            password='testing123',

            )
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token=data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.delete(
                '/api/v2/auth/logout',
                content_type='application/json',
                headers=headers

            )
            res3 = self.client.post(
                '/api/v2/auth/signup',
                data=json.dumps(user_toregister),
                content_type='application/json',
                headers=headers

            )

            response = json.loads(res3.data)
        self.assertEqual('token already revoked', response.get('msg'))


    def test_user_logout(self):                    
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
                '/api/v2/auth/logout',
                content_type='application/json',
                headers=headers

            )
            response = json.loads(res2.data)
        self.assertEqual('You have successfully logged out', response.get('message'))

        
