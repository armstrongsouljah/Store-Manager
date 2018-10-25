import unittest
import json

from flask_jwt_extended import create_access_token
from app import app
from app.models.users import User

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.obj = User(user_id=1, username='soultech', admin=True, password='password')
        self.client = app.test_client(self)


    def test_instantiation(self):
        self.assertIsInstance(self.obj, User)

    def test_admin_registers_user(self):
        with app.app_context():
            token = create_access_token('admin')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.post(
                 '/api/v1/users',
                 content_type='application/json',
                 data=json.dumps(self.obj.__dict__),
                 headers=headers
            )
            data = json.loads(res.data)
            self.assertEqual('User created successfully', data['msg'])

    def test_only_admin_accesses_user_records(self):
        with app.app_context():
            token = create_access_token('attendant')
            headers = {'Authorization': f'Bearer {token}'}
            res = self.client.get(
                '/api/v1/users',
                content_type='application/json',
                headers=headers
            )
            data = json.loads(res.data)
            self.assertEqual('Access for admins only', data['error'])