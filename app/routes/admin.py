from flask import Blueprint
from flask_login import current_user
from app.services.auth import role_required
from app.models.user import UserRole

bp = Blueprint("admin", __name__)

@bp.route("/")
@role_required(UserRole.ADMIN)
def admin_dashboard():
    return f"Bem-vindo ao painel do administrador, {current_user.name}"

@bp.route('/stores')
def manage_stores():
    return "Gerenciamento de Lojas"

@bp.route('/payments')
def manage_payments():
    return "Monitoramento de Pagamentos e Planos"
