import string
from flask import request
from app.utils import get_item_id, is_empty, validate_username

class User:
    """ stores user details """
    def __init__(self, user_id, username, admin=False, password=None):
        self.user_id = int(user_id)
        self.username = str(validate_username(username))
        self.admin = bool(admin)
        self.password = str(password)

    def register_user(self, **kwargs):
        # user_data = request.get_json()
        pass

    

    @property
    def is_admin(self):
        return self.admin