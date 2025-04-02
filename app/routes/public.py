from app.services import login_user_service, StoreOwnerRegistrationForm, create_store_owner
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import logout_user
from app.models import User
import json
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
    form = StoreOwnerRegistrationForm()

    if form.validate_on_submit():
        user, store = create_store_owner(form)
        if user and store:
            return redirect(url_for("dashboard.dashboard_home"))

    return render_template("public/register_store_owner.html", form=form)

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


