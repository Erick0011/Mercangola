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
         {"id": 1, "nome": "Produto 1", "preco": 1000,
         "imagem_url": url_for('static', filename='images/produto (1).avif')},
        {"id": 2, "nome": "Produto 2", "preco": 2000,
         "imagem_url": url_for('static', filename='images/produto (2).avif')},
        {"id": 3, "nome": "Produto 3", "preco": 3000,
         "imagem_url": url_for('static', filename='images/produto (3).avif')},
        {"id": 4, "nome": "Produto 4", "preco": 4000,
         "imagem_url": url_for('static', filename='images/produto (4).avif')},
        {"id": 5, "nome": "Produto 5", "preco": 5000,
         "imagem_url": url_for('static', filename='images/produto (5).avif')},
        {"id": 6, "nome": "Produto 6", "preco": 6000,
         "imagem_url": url_for('static', filename='images/produto (6).avif')},
        {"id": 7, "nome": "Produto 7", "preco": 7000,
         "imagem_url": url_for('static', filename='images/produto (7).avif')},
        {"id": 8, "nome": "Produto 8", "preco": 8000,
         "imagem_url": url_for('static', filename='images/produto (8).avif')},
        {"id": 9, "nome": "Produto 9", "preco": 9000,
         "imagem_url": url_for('static', filename='images/produto (9).avif')},
        {"id": 10, "nome": "Produto 10", "preco": 10000,
         "imagem_url": url_for('static', filename='images/produto (10).avif')},
        {"id": 11, "nome": "Produto 11", "preco": 11000,
         "imagem_url": url_for('static', filename='images/produto (11).avif')},
        {"id": 12, "nome": "Produto 12", "preco": 12000,
         "imagem_url": url_for('static', filename='images/produto (12).avif')},
        {"id": 13, "nome": "Produto 13", "preco": 13000,
         "imagem_url": url_for('static', filename='images/produto (13).avif')},
        {"id": 14, "nome": "Produto 14", "preco": 14000,
         "imagem_url": url_for('static', filename='images/produto (14).avif')},
        {"id": 15, "nome": "Produto 15", "preco": 15000,
         "imagem_url": url_for('static', filename='images/produto (15).avif')},
        {"id": 16, "nome": "Produto 16", "preco": 16000,
         "imagem_url": url_for('static', filename='images/produto (16).avif')},
        {"id": 17, "nome": "Produto 17", "preco": 17000,
         "imagem_url": url_for('static', filename='images/produto (17).avif')},
        {"id": 18, "nome": "Produto 18", "preco": 18000,
         "imagem_url": url_for('static', filename='images/produto (18).avif')},
        {"id": 19, "nome": "Produto 19", "preco": 19000,
         "imagem_url": url_for('static', filename='images/produto (19).avif')},
        {"id": 20, "nome": "Produto 20", "preco": 20000,
         "imagem_url": url_for('static', filename='images/produto (20).avif')},
        {"id": 21, "nome": "Produto 21", "preco": 21000,
         "imagem_url": url_for('static', filename='images/produto (21).avif')},
        {"id": 22, "nome": "Produto 22", "preco": 22000,
         "imagem_url": url_for('static', filename='images/produto (1).avif')},
        {"id": 23, "nome": "Produto 23", "preco": 23000,
         "imagem_url": url_for('static', filename='images/produto (2).avif')},
        {"id": 24, "nome": "Produto 24", "preco": 24000,
         "imagem_url": url_for('static', filename='images/produto (3).avif')},
        {"id": 25, "nome": "Produto 25", "preco": 25000,
         "imagem_url": url_for('static', filename='images/produto (4).avif')},
        {"id": 26, "nome": "Produto 26", "preco": 26000,
         "imagem_url": url_for('static', filename='images/produto (5).avif')},
        {"id": 27, "nome": "Produto 27", "preco": 27000,
         "imagem_url": url_for('static', filename='images/produto (6).avif')},
        {"id": 28, "nome": "Produto 28", "preco": 28000,
         "imagem_url": url_for('static', filename='images/produto (7).avif')},
        {"id": 29, "nome": "Produto 29", "preco": 29000,
         "imagem_url": url_for('static', filename='images/produto (8).avif')},
        {"id": 30, "nome": "Produto 30", "preco": 30000,
         "imagem_url": url_for('static', filename='images/produto (9).avif')},
        {"id": 31, "nome": "Produto 31", "preco": 31000,
         "imagem_url": url_for('static', filename='images/produto (10).avif')},
        {"id": 32, "nome": "Produto 32", "preco": 32000,
         "imagem_url": url_for('static', filename='images/produto (11).avif')},
        {"id": 33, "nome": "Produto 33", "preco": 33000,
         "imagem_url": url_for('static', filename='images/produto (12).avif')},
        {"id": 34, "nome": "Produto 34", "preco": 34000,
         "imagem_url": url_for('static', filename='images/produto (13).avif')},
        {"id": 35, "nome": "Produto 35", "preco": 35000,
         "imagem_url": url_for('static', filename='images/produto (14).avif')},
        {"id": 36, "nome": "Produto 36", "preco": 36000,
         "imagem_url": url_for('static', filename='images/produto (15).avif')},
        {"id": 37, "nome": "Produto 37", "preco": 37000,
         "imagem_url": url_for('static', filename='images/produto (16).avif')},
        {"id": 38, "nome": "Produto 38", "preco": 38000,
         "imagem_url": url_for('static', filename='images/produto (17).avif')},
        {"id": 39, "nome": "Produto 39", "preco": 39000,
         "imagem_url": url_for('static', filename='images/produto (18).avif')},
        {"id": 40, "nome": "Produto 40", "preco": 40000,
         "imagem_url": url_for('static', filename='images/produto (19).avif')},
        {"id": 41, "nome": "Produto 41", "preco": 41000,
         "imagem_url": url_for('static', filename='images/produto (20).avif')},
        {"id": 42, "nome": "Produto 42", "preco": 42000,
         "imagem_url": url_for('static', filename='images/produto (21).avif')},
        {"id": 43, "nome": "Produto 43", "preco": 43000,
         "imagem_url": url_for('static', filename='images/produto (1).avif')},
        {"id": 44, "nome": "Produto 44", "preco": 44000,
         "imagem_url": url_for('static', filename='images/produto (2).avif')},
        {"id": 45, "nome": "Produto 45", "preco": 45000,
         "imagem_url": url_for('static', filename='images/produto (3).avif')},
        {"id": 46, "nome": "Produto 46", "preco": 46000,
         "imagem_url": url_for('static', filename='images/produto (4).avif')},
        ]


    produtos_destaque = [produto for produto in produtos if produto['id'] in [1, 7]]

    loja_nome = tenant
    cor_principal = "#FFD700"   # Amarelo
    cor_secundaria = "#FF4500"  # Laranja
    cor_botao = "#FF6347"       # usado no hover do botaoVermelho
    cor_texto = "#1A1A1A"       # Branco


    return render_template(
        "store/pages/home.html",
        loja_nome=loja_nome,
        cor_principal=cor_principal,
        cor_secundaria=cor_secundaria,
        cor_botao=cor_botao,
        cor_texto=cor_texto,
        categorias=categorias,
        produtos=produtos,
        produtos_destaque=produtos_destaque
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

