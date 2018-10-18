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
token_expire_at = datetime.timedelta(minutes=75)

@bp.route('/login', methods=["POST"])
def login():
    auth = request.get_json()
    username = auth.get("username")
    password = auth.get("password")

    if not username and not password:
        return jsonify({"message":"enter your credentials"}), 401

    access_token = create_access_token(identity=username)

    if username == admin_user.username and password == admin_user.password:
        is_admin = admin_user.is_admin        
        return jsonify({"message":"logged in as admin", "admin":is_admin, "access_token": access_token}), 200

    if username == admin_user.username and password != admin_user.password:
        return jsonify({"message":"Invalid username/password"}), 401

    # authenticate attendant
    if username == attendant.username and password == attendant.password:
        # create a token here
        is_attendant = attendant.is_admin
        return jsonify({"message":"logged in as attendant", "admin":is_attendant, "access_token": access_token}), 200

    if username == attendant.username and password != attendant.password:
        return jsonify({"message":"Invalid username/password"}), 401