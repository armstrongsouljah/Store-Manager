import os

from flask import Flask
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from .config import env_config
from .utils import bp, welcome_message


def create_app_environment(config_name):
    """ declares app environment """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    return app


app = create_app_environment('app.config.TestingConfig')
from app.views.product_views import ProductsView
from app.views.auth import UserLoginView, UserRegisterView


jwt = JWTManager(app)

# welcome route
@app.route("/", methods=["GET"])
@jwt_required
def index():
    return welcome_message

app.add_url_rule('/api/v1/auth/login', view_func=UserLoginView.as_view('login'),\
                              methods=['POST'] )
signup_view = jwt_required(UserRegisterView.as_view('register'))
app.add_url_rule('/api/v1/auth/signup', \
                view_func=signup_view, methods=['POST'])

product_admin_view = jwt_required(ProductsView.as_view('products'))
products_fetch = ProductsView.as_view('productlist')
app.add_url_rule('/api/v1/products', view_func=products_fetch, methods=['GET'])
app.add_url_rule('/api/v1/products/<int:productId>', view_func=products_fetch, methods=['GET'])
app.add_url_rule('/api/v1/products', view_func=product_admin_view, methods=['POST'])
app.add_url_rule('/api/v1/products/<int:productId>', view_func=product_admin_view, methods=['PUT', 'DELETE'])



# # sales views
# sale_view = jwt_optional(Sales.as_view('sales'))
# app.add_url_rule('/api/v1/sales', view_func=sale_view, methods=['GET'])
# app.add_url_rule('/api/v1/sales', view_func=sale_view, methods=['POST'])
# app.add_url_rule('/api/v1/sales/<int:saleId>', \
#                      view_func=sale_view, methods=['GET'])



app.register_blueprint(bp, url_prefix='/api/v1')
