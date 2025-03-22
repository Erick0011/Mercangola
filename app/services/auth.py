from flask import redirect, url_for, request
from flask_login import login_user
from app.models.user import User, UserRole

def login_user_service(user, remember=False):
    """Autentica o usuário e redireciona com base na role"""
    login_user(user, remember=remember)

    # Redireciona com base no tipo de usuário
    if user.role == UserRole.ADMIN:
        return redirect(url_for("admin.admin_dashboard"))
    elif user.role == UserRole.STORE_OWNER:
        return redirect(url_for("dashboard.dashboard_home"))
    elif user.role == UserRole.CLIENT:
        # Tenta pegar a última URL visitada pelo cliente antes do login
        next_page = request.args.get("next")
        return redirect(next_page or url_for("store.store_home"))

    return redirect(url_for("public.home"))  # Caso de fallback
