import uuid
from datetime import timedelta



def create_store_with_owner(name, email, password, store_name, slug):
    from app.models import Store, StoreAccount, StorePlan, StoreAccessLevel, UserRole
    from app.extensions import db
    from app.services import get_local_time
    """
    Cria uma loja com seu proprietário (StoreAccount).
    """
    # Criar loja
    store = Store(
        name=store_name,
        slug=slug,
        tenant_id=str(uuid.uuid4()),
        email=email,
        plan=StorePlan.TRIAL,
        expiration_date=get_local_time() + timedelta(days=7),
    )

    # Criar usuário StoreOwner
    user = StoreAccount(
        name=name,
        email=email,
        role=UserRole.STORE_OWNER,
        store=store,
        store_access_level=StoreAccessLevel.OWNER,
    )
    user.set_password(password)

    # Salvar no banco
    db.session.add(store)
    db.session.add(user)
    db.session.commit()

    return user  # ou store, ou ambos, conforme sua necessidade
