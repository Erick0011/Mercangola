from app.extensions import db
from datetime import datetime, timezone
from app.models.user import User
from enum import Enum


# Enum para os planos disponíveis
class StorePlan(Enum):
    BASIC = "basic"
    PROFESSIONAL = "professional"
    ADVANCED = "advanced"
    ENTERPRISE = "enterprise"

# Enum para o tipo de loja
class StoreType(Enum):
    PHYSICAL = "physical"
    DIGITAL = "digital"
    BOTH = "both"

class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tenant_id = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # FK para User
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Contato
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    website = db.Column(db.String(255), nullable=True)

    # Endereço
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    # Redes Sociais
    facebook = db.Column(db.String(255), nullable=True)
    instagram = db.Column(db.String(255), nullable=True)
    twitter = db.Column(db.String(255), nullable=True)
    whatsapp = db.Column(db.String(20), nullable=True)

    # Plano da Loja
    plan = db.Column(db.Enum(StorePlan), default=StorePlan.BASIC, nullable=False)
    subscription_fee = db.Column(db.Float, default=0.0, nullable=False)  # Mensalidade do plano escolhido
    expiration_date = db.Column(db.DateTime, nullable=False)  # Data de expiração do plano

    # Tipo de Loja (Produtos físicos, digitais ou ambos)
    store_type = db.Column(db.Enum(StoreType), default=StoreType.BOTH, nullable=False)

    # Controle
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)

    # Relacionamento com o usuário
    owner = db.relationship('User', backref=db.backref('stores', lazy=True))

    def check_expiration(self):
        """Atualiza o status da loja se a assinatura expirou."""
        if self.expiration_date < datetime.now(timezone.utc):
            self.is_active = False

    def __repr__(self):
        return f"<Store {self.name} - Plan: {self.plan.value}>"


