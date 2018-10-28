import json
from .base import BaseTestCase


class TestUsers(BaseTestCase):

    def test_userlogin(self):

        with self.app.app_context():
            res = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
        self.assertIn(b'Logged in successfully', res.data)
    
    def test_invalid_details(self):
        self.user['username'] = ""
        with self.app.app_context():
            res = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
        self.assertIn(b'invalid username/password try again', res.data)
