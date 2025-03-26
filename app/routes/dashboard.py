from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from app.services.auth import role_required
from app.models.user import UserRole

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@role_required(UserRole.STORE_OWNER)
def dashboard_home():
    return render_template("dashboard/base_dashboard.html")

@bp.route('/products')
def manage_products():
    return "Gerenciamento de Produtos"

@bp.route('/settings')
def store_settings():
    return "Configurações da Loja"
