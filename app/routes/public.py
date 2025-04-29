from app.services import login_user_service, StoreOwnerRegistrationForm, create_store_owner
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import logout_user
from app.models import User
import json
import re
import os

bp = Blueprint("public", __name__)

@bp.route("/")
def home():
    return render_template("public/home.html")

@bp.route("/forgot_password")
def forgot_password():
    return "Melhor lembrar, Pq na tem função de recuperar"

@bp.route("/register")
def register():
    return "Em construção"


@bp.route("/register_store_owner", methods=["GET", "POST"])
def register_store_owner():

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        store_name = request.form.get('store_name', '').strip()
        slug = request.form.get('slug', '').strip()
        accepted_terms = request.form.get('condition')

        errors = []

        # Nome
        if not name:
            errors.append("Digite seu nome.")

        # Email
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Digite um email válido.")

        # Senha
        if len(password) < 8:
            errors.append("A senha deve ter pelo menos 8 caracteres.")
        elif password != confirm_password:
            errors.append("As senhas não coincidem.")

        # Nome da loja
        if not store_name:
            errors.append("Digite o nome da loja.")

        # Slug
        if not slug:
            errors.append("Slug inválido.")

        # Termos
        if not accepted_terms:
            errors.append("Você precisa aceitar os termos.")

        if errors:
            for error in errors:
                flash(error, 'danger')
            return redirect(url_for('public.register_store_owner'))

        flash("Formulário válido! (Salvar depois)", 'success')
        return redirect(url_for('public.register_store_owner'))

    return render_template("public/register_store_owner.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return login_user_service(user)
        print('Algo errado')
        flash("Credenciais inválidas!", "error")

    return render_template("public/login.html")

@bp.route('/get-angola_data', methods=['GET'])
def get_angola_data():
    json_path = os.path.join(os.getcwd(), "app", "static", "vendor", "json_files", "angola_data.json")

    if not os.path.exists(json_path):
        return jsonify({"error": "Arquivo JSON não encontrado"}), 500

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            angola_data = json.load(file)
        return jsonify(angola_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("public.login"))


