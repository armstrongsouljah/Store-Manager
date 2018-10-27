import os
from flask import Flask
from app.models.products import Product
from app.models.sales import Sale
from app.views.authviews import *
from app.views.productviews import *
from app.views.salesviews import *
from .config import env_config
from .utils import bp,  welcome_message
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# bp = Blueprint('api', __name__)


def create_app_environment(config_name):
    """ declares app environment """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    return app


app = create_app_environment('app.config.DevelopmentConfig')

jwt = JWTManager(app)
# welcome route
@app.route("/", methods=["GET"])
def index():
    return welcome_message

# sales views
sale_view = jwt_optional(Sales.as_view('sales'))
app.add_url_rule('/api/v1/sales', view_func=sale_view, methods=['GET'])
app.add_url_rule('/api/v1/sales', view_func=sale_view, methods=['POST'])
app.add_url_rule('/api/v1/sales/<int:saleId>', \
                     view_func=sale_view, methods=['GET'])

# products views
product_view = jwt_optional(ProductsView.as_view('products'))
app.add_url_rule('/api/v1/products', view_func=product_view, methods=['GET'])
app.add_url_rule('/api/v1/products', view_func=product_view, methods=['POST'])
app.add_url_rule('/api/v1/products/<int:productId>', \
                     view_func=product_view, methods=['GET', 'PUT', 'DELETE'])

# user registration and retrieval
user_view = jwt_required(UserView.as_view('users'))
app.add_url_rule('/api/v1/users',view_func=user_view, methods=['GET','POST'])

app.register_blueprint(bp, url_prefix='/api/v1')
