from app.extensions import db
from app.services import get_local_time

# 📈 Visualizações da loja - mede tráfego geral da loja
class StoreView(db.Model):
    __tablename__ = 'store_views'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), index=True, nullable=False)
    viewed_at = db.Column(db.DateTime, default=get_local_time())
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

# 📈 Visualizações do produto
class ProductView(db.Model):
    __tablename__ = 'product_views'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.Text)
    viewed_at = db.Column(db.DateTime, default=get_local_time())

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)


# 🔍 Buscas feitas dentro da loja - útil para entender interesses dos clientes
class SearchQuery(db.Model):
    __tablename__ = 'search_queries'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), index=True, nullable=False)
    query = db.Column(db.String(255), nullable=False)
    searched_at = db.Column(db.DateTime, default=get_local_time())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)


# 🛒 Carrinhos abandonados - permite análise e futuras campanhas de recuperação
class CartAbandonment(db.Model):
    __tablename__ = 'cart_abandonments'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    products = db.Column(db.JSON)  # lista de produtos com ID, nome, qty, etc.
    abandonado_em = db.Column(db.DateTime, default=get_local_time())


# 🔗 Produto compartilhado - mede o "engajamento social" dos produtos
class ProductShare(db.Model):
    __tablename__ = 'produto_shares'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), index=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    shared_at = db.Column(db.DateTime, default=get_local_time())
    platform = db.Column(db.String(50))  # WhatsApp, Instagram, etc


# 🖱️ Clicks em ações importantes nos produtos
class ProductClickEvent(db.Model):
    __tablename__ = 'produto_click_events'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), index=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    event_type = db.Column(db.String(50))  # ex: 'add_to_cart', 'buy_now'
    clicked_at = db.Column(db.DateTime, default=get_local_time())


# 🧠 Log geral do sistema - para ti como criador acompanhar o uso da plataforma
class SystemLog(db.Model):
    __tablename__ = 'system_logs'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), index=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    action = db.Column(db.String(255))     # Ex: "Created Product", "Updated Store"
    route = db.Column(db.String(255))      # Ex: "/store/slug/produto/123"
    created_at = db.Column(db.DateTime, default=get_local_time())
