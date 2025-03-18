from flask import Blueprint

bp = Blueprint('store', __name__)

@bp.route('/<string:tenant>/')
def store_home(tenant):
    return f"Página inicial da loja {tenant}"

@bp.route('/<string:tenant>/products')
def store_products(tenant):
    return f"Lista de produtos da loja {tenant}"

@bp.route('/<string:tenant>/product/<int:product_id>')
def store_product_detail(tenant, product_id):
    return f"Página do produto {product_id} da loja {tenant}"
