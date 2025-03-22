from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user
from app.models.user import User
from app.services.auth import login_user_service

bp = Blueprint("public", __name__)

@bp.route("/")
def home():
    return render_template("public/home.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return login_user_service(user)

        flash("Credenciais inválidas!", "error")

    return render_template("public/login.html")

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("public.login"))


