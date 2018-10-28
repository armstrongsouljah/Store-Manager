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
            message = {'msg' : create_access_token(identity=returned_user['admin'], expires_delta=day), 'success':'Logged in successfully'}
        else:
            message = {'msg': 'invalid username/password try again'}
        return jsonify(message)



class UserRegisterView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        response = None

        admin_status = get_jwt_identity()
        if admin_status == True:
            response = user_obj.register_user(username, password)
        else:
            response = {'msg': 'Access only for admins'}
        return jsonify(response)
