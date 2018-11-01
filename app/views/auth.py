import datetime
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models.users import User

user_obj = User()

class UserLoginView(MethodView):
    def post(self):
        data =  request.get_json()
        username = data.get('username')
        password = data.get("password")
        returned_user = None

        if username:
            returned_user = user_obj.authenticate(username, password=password)
        
        if not username:
            message = {'msg': 'please enter username'}
            
        if username and not username.isspace():
            message ={'msg':'Please enter valid username'}

        if returned_user is not None:
            pwd = returned_user.get('password')
        else:
            pwd = ''
        if pwd and check_password_hash(pwd, password):
            day = datetime.timedelta(days=1)
            my_identity=dict(
                user_id=returned_user.get('user_id'),
                user_role=returned_user.get('role')
            )
            message = {'msg' : create_access_token(identity=my_identity, expires_delta=day), 'success':'Logged in successfully'}
        else:
            message = {'msg': 'invalid username/password try again'}
        return jsonify(message)



class UserRegisterView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        response = None

        admin_status = get_jwt_identity()
        if admin_status['user_role'] == 'admin':
            response = user_obj.register_user(username, password, role)
        else:
            response = {'msg': 'Access only for admins'}
        return jsonify(response)
