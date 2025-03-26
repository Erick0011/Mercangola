from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from app.services.auth import role_required
from app.models.user import UserRole

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@role_required(UserRole.STORE_OWNER)
def dashboard_home():
    return render_template("dashboard/base_dashboard.html")

@bp.route("/get_data")
def get_data():
    # Simulação de dados do banco de dados
    data = {
        "faturamento_total": 1500000,
        "pedidos_hoje": 12,
        "produtos_ativos": 35,
        "pedidos": [
            {"id": "#001", "cliente": "João Silva", "valor": "KZ 12.500", "status": "Concluído", "data": "23/03/2025"},
            {"id": "#002", "cliente": "Maria Santos", "valor": "KZ 8.200", "status": "Pendente", "data": "23/03/2025"},
            {"id": "#003", "cliente": "Débora Tchissola", "valor": "KZ 19.200", "status": "Pendente", "data": "25/03/2025"}
        ],
        "grafico_faturamento": [200000, 180000, 250000, 220000, 300000, 350000, 400000],
        "grafico_pedidos": [50, 80, 40, 70],
        "grafico_categorias": [40, 30, 20, 10],
        "grafico_crescimento": [5, 7, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55],
        "grafico_regioes": [50000, 30000, 20000, 15000, 10000]
    }
    return jsonify(data)

@bp.route('/products')
def manage_products():
    return "Gerenciamento de Produtos"

@bp.route('/settings')
def store_settings():
    return "Configurações da Loja"
