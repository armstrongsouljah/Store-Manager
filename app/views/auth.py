from flask import request, jsonify
from flask.views import MethodView

from app.models.users import User

user_obj = User()

class UserLoginView(MethodView):
    def post(self):
        data =  request.get_json()
        username = data['username']
        return user_obj.get_all()