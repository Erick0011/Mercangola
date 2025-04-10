from app.extensions import db
from datetime import datetime, timedelta
from app.services import get_local_time
from app.models import CartItem, CartAbandonment, User


def detect_abandoned_carts(tenant_id, limite_em_horas=12):
    agora = get_local_time()
    limite = agora - timedelta(hours=limite_em_horas)

    # Filtra os itens do carrinho que foram adicionados há mais de X horas e ainda não foram processados
    cart_items = CartItem.query.filter(
        CartItem.tenant_id == tenant_id,
        CartItem.added_at < limite,
        CartItem.processed == False  # Garante que os itens ainda não foram processados
    ).all()

    # Organiza por usuário
    carts = {}
    for item in cart_items:
        # Atualiza o 'last_seen' do usuário para indicar que houve atividade
        item.user.last_seen = agora
        db.session.commit()

        # Verifica se o usuário já foi adicionado ao dicionário de carrinhos
        if item.user_id not in carts:
            carts[item.user_id] = {
                "usuario": item.user,
                "produtos": []
            }
        carts[item.user_id]["produtos"].append(item.product)

        # Marca o item como processado
        item.processed = True
        db.session.commit()

    # Salva no log de abandono de carrinho
    for user_id, dados in carts.items():
        products_list = [produto.name for produto in dados["produtos"]]  # Exemplo de como armazenar a lista de produtos
        abandonment_log = CartAbandonment(
            user_id=dados['usuario'].id,
            tenant_id=tenant_id,
            products=str(products_list)  # Armazenando os produtos como uma string (pode também ser JSON)
        )
        db.session.add(abandonment_log)

    db.session.commit()

    return carts

"""
# Detectando carrinhos abandonados
abandonados = detect_abandoned_carts(tenant_id='loja-123', limite_em_horas=6)

# Exibindo carrinhos abandonados
for user_id, dados in abandonados.items():
    print(f"Usuário {dados['usuario'].name} abandonou:")
    for produto in dados["produtos"]:
        print(f" - {produto.name}")

"""
