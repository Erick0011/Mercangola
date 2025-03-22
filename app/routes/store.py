from flask import Blueprint
from flask_login import current_user, login_required
from app.services.auth import role_required
from app.models.user import UserRole

bp = Blueprint("store", __name__)

# 🔓 Páginas abertas (acessíveis para qualquer usuário)
@bp.route("/<string:tenant>/")
def store_home(tenant):
    user_name = f", {current_user.name}" if current_user.is_authenticated else ""
    return f"Bem-vindo à loja {tenant}{user_name}"

@bp.route("/<string:tenant>/products")
def store_products(tenant):
    user_name = f", {current_user.name}" if current_user.is_authenticated else ""
    return f"Lista de produtos da loja {tenant}{user_name}"

@bp.route("/<string:tenant>/product/<int:product_id>")
def store_product_detail(tenant, product_id):
    user_name = f", {current_user.name}" if current_user.is_authenticated else ""
    return f"Página do produto {product_id} da loja {tenant}{user_name}"

# 🔒 Páginas protegidas (apenas CLIENTES logados podem acessar)
@bp.route("/<string:tenant>/cart")
@login_required
@role_required(UserRole.CLIENT)
def store_cart(tenant):
    return f"Carrinho de compras da loja {tenant}, {current_user.name}"

@bp.route("/<string:tenant>/checkout")
@login_required
@role_required(UserRole.CLIENT)
def store_checkout(tenant):
    return f"Página de checkout da loja {tenant}, {current_user.name}"

