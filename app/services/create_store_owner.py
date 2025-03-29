from app.models import Store, StorePlan, User, UserRole
from datetime import datetime, timedelta, timezone
from flask import flash
from app.extensions import db
from werkzeug.security import generate_password_hash


def create_store_owner(form):
    """
    Cria um novo usuário do tipo STORE_OWNER e sua loja correspondente.

    Args:
        form: O formulário contendo os dados do lojista e da loja.

    Returns:
        user (User): O usuário criado.
        store (Store): A loja criada.
    """
    try:
        # Criar o usuário (Store Owner)
        user = User(
            name=form.name.data,
            email=form.email.data,
            telefone=form.telefone.data,
            role=UserRole.STORE_OWNER
        )
        user.set_password(form.password.data)  # Hash da senha

        db.session.add(user)
        db.session.commit()  # Salvar para obter o user_id

        # Criar a loja vinculada ao usuário com 7 dias grátis no plano básico
        store = Store(
            tenant_id=form.slug.data,
            slug=form.slug.data,
            owner_id=user.id,
            name=form.store_name.data,
            description=form.description.data,
            phone=form.phone.data,
            email=form.email_store.data,
            website=form.website.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            country=form.country.data,
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            facebook=form.facebook.data,
            instagram=form.instagram.data,
            twitter=form.twitter.data,
            whatsapp=form.whatsapp.data,

            # 7 dias grátis no plano básico
            plan=StorePlan.BASIC,
            subscription_fee=0.0,
            expiration_date=datetime.now(timezone.utc) + timedelta(days=7),

            store_type=form.store_type.data,
        )

        db.session.add(store)
        db.session.commit()  # Salvar a loja

        flash("Loja criada com sucesso! Você tem 7 dias grátis no plano Básico.", "success")

        return user, store  # Retorna os objetos criados

    except Exception as e:
        db.session.rollback()  # Reverte alterações em caso de erro
        flash(f"Ocorreu um erro ao criar a conta: {str(e)}", "danger")
        return None, None  # Retorna None em caso de falha
