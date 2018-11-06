import os

from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from .config import env_config
from .utils import bp, welcome_message


def create_app_environment(config_name):
    """ declares app environment """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    return app


# app = create_app_environment('app.config.ProductionConfig')
app = create_app_environment('app.config.TestingConfig')

# allow ajax requests.
CORS(app)

from app.views.product_views import ProductsView
from app.views.auth import UserLoginView, UserRegisterView
from app.views.sales_views import SalesView


jwt = JWTManager(app)

# welcome route
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


    

app.add_url_rule('/api/v2/auth/login', view_func=UserLoginView.as_view('login'),\
                              methods=['POST'] )
signup_view = jwt_required(UserRegisterView.as_view('register'))
app.add_url_rule('/api/v2/auth/signup', \
                view_func=signup_view, methods=['POST'])

product_admin_view = jwt_required(ProductsView.as_view('products'))
products_fetch = ProductsView.as_view('productlist')
app.add_url_rule('/api/v2/products', view_func=products_fetch, methods=['GET'])
app.add_url_rule('/api/v2/products/<int:productId>', view_func=products_fetch, methods=['GET'])
app.add_url_rule('/api/v2/products', view_func=product_admin_view, methods=['POST'])
app.add_url_rule('/api/v2/products/<int:productId>', view_func=product_admin_view, methods=['PUT', 'DELETE'])

make_sale = jwt_required(SalesView.as_view('sale_add'))
get_all_sales = jwt_required(SalesView.as_view('records'))
filter_by_attendant = jwt_required(SalesView.as_view('filtered_list'))
app.add_url_rule('/api/v2/sales', view_func=make_sale, methods=['POST'])
app.add_url_rule('/api/v2/sales', view_func=get_all_sales, methods=['GET'] )
app.add_url_rule('/api/v2/sales/<int:attendant_id>', view_func=filter_by_attendant, methods=['GET'] )

app.register_blueprint(bp, url_prefix='/api/v2')
