import os

from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, get_raw_jwt, jwt_required, jwt_optional)

from .config import env_config
from .utils import bp, fetch_all, check_item_exists


def create_app_environment(config_name):
    """ declares app environment """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    return app


# app = create_app_environment('app.config.ProductionConfig')
app = create_app_environment('app.config.TestingConfig')


# allow ajax requests.
CORS(app)

from app.models.users import User
from app.views.category_views import CategoryViews
from app.views.product_views import ProductsView
from app.views.auth import UserLoginView, UserLogoutView, UserRegisterView, \
                    UserListView
from app.views.sales_views import SalesView

user_obj = User()

blacklist = set()

jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

# welcome route
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html') # pragma no cover

app.add_url_rule('/api/v2/auth/login', view_func=UserLoginView.as_view('login'),\
                              methods=['POST'] )
signup_view = jwt_required(UserRegisterView.as_view('register'))
app.add_url_rule('/api/v2/auth/signup', \
                view_func=signup_view, methods=['POST'])
app.add_url_rule('/api/v2/auth/logout', view_func=UserLogoutView.as_view('logout'), \
                               methods=['DELETE'])
app.add_url_rule('/api/v2/auth/users', view_func=UserListView.as_view('users'), methods=['GET'])
    

categoryaddview = jwt_required(CategoryViews.as_view('categoryadd'))
categorylistview = CategoryViews.as_view('categorylist')
categoryfetchview = jwt_optional(CategoryViews.as_view('categories'))
app.add_url_rule('/api/v2/categories', view_func=categoryaddview, methods=['POST'])
app.add_url_rule('/api/v2/categories', view_func=categorylistview, methods=['GET'])
app.add_url_rule('/api/v2/categories/<int:categoryId>', view_func=categoryfetchview, methods=['GET', 'PUT', 'DELETE'])

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
