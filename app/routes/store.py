from flask import Blueprint, render_template, url_for
from flask_login import current_user, login_required
from app.services.auth import role_required
from app.models.user import UserRole

bp = Blueprint("store", __name__)


@bp.route("/<string:tenant>/")
def store_home(tenant):
    categorias = [
        {"nome": "Eletrônicos", "icon": "tv"},
        {"nome": "Roupas", "icon": "tshirt"},
        {"nome": "Alimentos", "icon": "apple-alt"},
        {"nome": "Eletrônicos", "icon": "tv"},
        {"nome": "Roupas 2", "icon": "tshirt"},

    ]

    produtos = [
        {"id": 1, "nome": "Fone Bluetooth", "preco": 12000, "imagem_url": url_for('static', filename='images/placeholder-images-image_large.webp')
        },
        { "id": 2, "nome": "Camisa Estilosa", "preco": 6500, "imagem_url": url_for('static', filename='images/placeholder-images-image_large.webp')
        },
        {"id": 3, "nome": "Liquidificador", "preco": 18000, "imagem_url": url_for('static', filename='images/placeholder-images-image_large.webp')
        },
        {"id": 4, "nome": "Livro JavaScript", "preco": 7200, "imagem_url": url_for('static', filename='images/placeholder-images-image_large.webp')
        },
    ]
    loja_nome = tenant
    cor_principal = "#FFD700"   # Amarelo
    cor_secundaria = "#FF4500"  # Laranja
    cor_botao = "#DC3545"       # Vermelho

    return render_template(
        "store/pages/home.html",
        loja_nome=loja_nome,
        cor_principal=cor_principal,
        cor_secundaria=cor_secundaria,
        cor_botao=cor_botao,
        categorias=categorias,
        produtos=produtos
    )

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

