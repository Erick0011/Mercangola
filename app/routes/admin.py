from flask import Blueprint

bp = Blueprint('admin', __name__)

@bp.route('/')
def admin_home():
    return "Painel Administrativo - Gerenciamento de Lojistas"

@bp.route('/stores')
def manage_stores():
    return "Gerenciamento de Lojas"

@bp.route('/payments')
def manage_payments():
    return "Monitoramento de Pagamentos e Planos"
