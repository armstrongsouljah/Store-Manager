from flask import jsonify, request, make_response
from flask.views import MethodView
from app.utils import bp
import datetime
from app.config import DevelopmentConfig
from app.models.users import User

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


dev = DevelopmentConfig()
admin_user = User(user_id=1, username='admin', admin=True, password='password')
attendant = User(user_id=2, username='attendant', admin=False, password='password')
user_obj = User()
token_expire_at = datetime.timedelta(days=1)

@bp.route('/login', methods=["POST"])
def login():
    auth = request.get_json()
    username = auth.get("username")
    password = auth.get("password")
    access_token = create_access_token(identity=username, expires_delta=token_expire_at)

    if not username and not password:
        response = {"message":"enter your credentials"}, 401    

    if username == admin_user.username  and password == admin_user.password:     
        response = {"message":"logged in as admin", \
                        "access_token": access_token}, 200

    elif username == attendant.username and password == attendant.password:
        response = {"message":"logged in as attendant",\
                        "access_token": access_token}, 200
    else:
        response = ({"message":"Invalid username/password"} , 401)

    return jsonify(response)


class UserLogin(MethodView):
    def post(self):
        response = user_obj.get_users()
        return jsonify(response)

class UserView(MethodView):
    """ Handles creation and returnig of available users """

    def get(self):
        logged_in_user = get_jwt_identity()
        if logged_in_user != 'admin':
            response = {'error': 'Access for admins only'}
        else:
            response = user_obj.get_users()
        return jsonify(response)

    def post(self):
        current_user = get_jwt_identity()
        response = None
        if current_user != 'admin':
            response = {'error': 'Only admins can register new users.'}
        response = user_obj.register_user()
        return jsonify(response)
    
