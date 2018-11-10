import datetime
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_raw_jwt
from werkzeug.security import check_password_hash
from app.models.users import User
from app.utils import check_item_exists
from databases.server import DatabaseConnection

db_cursor = DatabaseConnection().cursor
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
        token_jti = get_raw_jwt()['jti']
        response = None

        user_identity = get_jwt_identity()
        is_revoked = check_item_exists('token_jti', 'blacklisted', token_jti, db_cursor )

        if is_revoked:
            return jsonify({'msg': 'token already revoked'}), 401
        if user_identity['user_role'] == 'admin':
            response = user_object.register_user(username, password, user_role)
            response = jsonify(response), 201
        else:
            response = {'message': 'Access only for admins'}
            response = jsonify(response), 401
        return response

class UserLogoutView(MethodView):
    @jwt_required
    def delete(self):
        token_jti = get_raw_jwt()['jti']
        response = user_object.do_the_logout(token_jti)
        return response

