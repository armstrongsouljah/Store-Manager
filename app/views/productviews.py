from app.models.products import Product
from app.api import bp

obj = Product()
    
@bp.route('/products', methods=['GET'])    
def get_products():        
    return obj.get_products()


@bp.route('/products/<int:product_id>')
def get_product(product_id):
    pass



@bp.route('/products/add', methods=['POST'])
def add_product():
    pass

