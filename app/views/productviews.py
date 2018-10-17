from app.utils import bp
from app.models.products import Product
from app.models.users import User
from flask import jsonify, request
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)

product_model = Product()
user1 = User(1,"armstrong", True, "hello")


    
@bp.route('/products', methods=['GET'])    
def get_products():
    response  = product_model.get_products()
    return jsonify(response)

@bp.route('/products', methods=['POST'])
# @jwt_required
def products_add():
    # current_user = get_jwt_identity()
    # if current_user:
    response = product_model.add_product()
    return jsonify(response)

# for later
@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    sample_user = User(1,"armstrong",True, "armstrong")
    if username !=sample_user.username and password != sample_user.password:
        return jsonify({"Message": "Bad username or password"})
        
    admin = sample_user.admin
    access_token = {'token':create_access_token(identity=username), 'admin':admin}
    
    return jsonify(access_token), 200
