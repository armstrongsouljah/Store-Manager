from flask import jsonify, request, make_response
from app.utils import bp
import datetime
from app.config import DevelopmentConfig
from app.models.users import User

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


dev = DevelopmentConfig()
admin_user = User(1, 'admin', True, 'password')
attendant = User(2,'attendant', False, 'password')
token_expire_at = datetime.timedelta(minutes=700)

@bp.route('/login', methods=["POST"])
def login():
    auth = request.get_json()
    username = auth.get("username")
    password = auth.get("password")
    access_token = create_access_token(identity=username)

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