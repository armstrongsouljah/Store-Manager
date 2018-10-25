import string
from flask import request
from app.utils import get_item_id, is_empty, validate_username
users = []
class User:
    """ stores user details """
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.admin = False
        self.password = kwargs.get("password")

    def register_user(self):
        """ allows store owner to register new users """

        user_data = request.get_json()
        user_name = user_data.get("username")
        password = user_data.get("password")

        new_user = User(user_id=get_item_id("user_id", users), username=user_name, admin=self.admin, password=password)
        response = None

        already_registered = [user for user in users if user['username']==user_name]
        if is_empty(already_registered):
            users.append(dict(new_user.__dict__))
            response = {'msg': 'User created successfully'}
            print(users)
        else:
            response = {'error':'User with that username already exists'}
        return response

    def get_users(self):
        if is_empty(users):
            response = {'message': 'No registered users at the moment.'}
        else:
            response = users
        return response
            

    

    @property
    def is_admin(self):
        return self.admin