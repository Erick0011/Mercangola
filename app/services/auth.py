from flask import redirect, url_for, request
from flask_login import login_user, current_user
from functools import wraps


def login_user_service(user, remember=False):
    from app.models.user import UserRole
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
        return redirect(next_page or url_for("store.store_home", tenant="Loja Padrão"))

    return redirect(url_for("public.home"))  # Caso de fallback

def role_required(role):
    """Restringe acesso a usuários com a role especificada"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                return redirect(url_for("public.login"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
