from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from app.services.auth import role_required
from app.models.user import UserRole
from app.models import Store, StoreCategory
from app.extensions import db

bp = Blueprint("dashboard", __name__)

@bp.route("/")
@role_required(UserRole.STORE_OWNER)
def dashboard_home():
    store = current_user.store
    user = current_user
    return render_template("dashboard/home.html", store=store, user=user)



@bp.route('/categorias', methods=['GET'])
@role_required(UserRole.STORE_OWNER)
def category_view():
    search = request.args.get('search', '')
    store = current_user.store
    user = current_user
    if search:
        categorias = StoreCategory.query.filter(
            StoreCategory.store_id == store.id,
            StoreCategory.name.ilike(f'%{search}%')
        ).all()
    else:
        categorias = StoreCategory.query.filter_by(store_id=store.id).all()
    return render_template('dashboard/category_view.html', categories=categorias, user=user)



@bp.route('/categorias/adicionar', methods=['POST'])
@role_required(UserRole.STORE_OWNER)
def add_category():
    nome = request.form.get('name')
    if nome:
        nova_categoria = StoreCategory(
            name=nome,
            store_id=current_user.store.id,
            tenant_id=current_user.store.tenant_id
        )
        db.session.add(nova_categoria)
        db.session.commit()
        flash('Categoria adicionada com sucesso!', 'success')
    else:
        flash('O nome da categoria obrigatório.', 'error')
    return redirect(url_for('dashboard.category_view'))

@bp.route('/categorias/editar/<int:categoria_id>', methods=['POST'])
@role_required(UserRole.STORE_OWNER)
def edit_category(categoria_id):
    categoria = StoreCategory.query.get_or_404(categoria_id)
    if categoria.store_id != current_user.store.id:
        flash('Você não tem permissão para editar esta categoria.', 'error')
        return redirect(url_for('dashboard.category_view'))
    nome = request.form.get('name')
    if nome:
        categoria.name = nome
        db.session.commit()
        flash('Categoria atualizada com sucesso!', 'success')
    else:
        flash('O nome da categoria  obrigatório.', 'error')
    return redirect(url_for('dashboard.category_view'))

@bp.route('/categorias/excluir/<int:categoria_id>', methods=['POST'])
@role_required(UserRole.STORE_OWNER)
def delete_category(categoria_id):
    categoria = StoreCategory.query.get_or_404(categoria_id)
    if categoria.store_id != current_user.store.id:
        flash('Você não tem permissão para excluir esta categoria.', 'error')
        return redirect(url_for('dashboard.category_view'))
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoria excluída com sucesso!', 'success')
    return redirect(url_for('dashboard.category_view'))




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
