from flask import Blueprint

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def dashboard_home():
    return "Painel do Lojista - Resumo das vendas"

@bp.route('/products')
def manage_products():
    return "Gerenciamento de Produtos"

@bp.route('/settings')
def store_settings():
    return "Configurações da Loja"
