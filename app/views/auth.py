import datetime
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models.users import User

user_object = User()

class UserLoginView(MethodView):
    def post(self):
        data =  request.get_json()
        username = data.get('username')
        password = data.get("password")
        returned_user = None

        if username:
            returned_user = user_object.fetch_user(username, password=password)
        
        if not username:
            response = {'message': 'please enter username'}
            
        if username and not username.isspace():
            response ={'message':'Please enter valid username'}

        if returned_user is not None:
            hashed_password = returned_user.get('password')
        else:
            hashed_password = ''
        if hashed_password and check_password_hash(hashed_password, password):
            token_expiry = datetime.timedelta(days=1)
            my_identity=dict(
                user_id=returned_user.get('user_id'),
                user_role=returned_user.get('role')
            )
            response = {'token' : create_access_token(identity=my_identity, expires_delta=token_expiry), 'message':'Logged in successfully'}
            response = jsonify(response), 200
        else:
            response = { 'token': None, 'message': 'invalid username/password try again'}
            response = jsonify(response), 401
        return response



class UserRegisterView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user_role = data.get('role')
        response = None

        user_identity = get_jwt_identity()
        if user_identity['user_role'] == 'admin':
            response = user_object.register_user(username, password, user_role)
            response = jsonify(response), 201
        else:
            response = {'message': 'Access only for admins'}
            response = jsonify(response), 401
        return response
