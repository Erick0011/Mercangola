from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from app.services.auth import role_required
from app.models.user import UserRole
from app.models import Store, Category, StoreCategory
from app.extensions import db

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@role_required(UserRole.STORE_OWNER)
def dashboard_home():
    return render_template("dashboard/home.html")

@bp.route('/escolher-categorias', methods=['GET', 'POST'])
@role_required(UserRole.STORE_OWNER)
def category_select():
    store = Store.query.filter_by(owner_id=current_user.id).first_or_404()
    todas_categorias = Category.query.all()

    if request.method == 'POST':
        selecionadas_ids = request.form.getlist('categories')

        # Apagar categorias antigas da loja
        StoreCategory.query.filter_by(store_id=store.id).delete()

        # Adicionar novas categorias selecionadas
        for cid in selecionadas_ids:
            nova = StoreCategory(
                store_id=store.id,
                tenant_id=store.tenant_id,  # pegando o tenant da store
                category_id=int(cid)
            )
            db.session.add(nova)

        db.session.commit()
        flash('Categorias atualizadas com sucesso!', 'success')
        return redirect(url_for('dashboard.category_select'))

    # Categorias que já estão cadastradas para essa loja
    categorias_atuais = [sc.category_id for sc in store.categories]

    return render_template('dashboard/category_select.html',
                           categorias=todas_categorias,
                           selecionadas=categorias_atuais,
                           store=store
                           )



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
