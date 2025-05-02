from app.extensions import db
from app.services import get_local_time
from enum import Enum

# Enum para os planos disponíveis
class StorePlan(Enum):
    TRIAL = "trial"
    BASIC = "basic"
    PROFESSIONAL = "professional"
    ADVANCED = "advanced"
    ENTERPRISE = "enterprise"


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    website = db.Column(db.String(255), nullable=True)

    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    facebook = db.Column(db.String(255), nullable=True)
    instagram = db.Column(db.String(255), nullable=True)
    tiktok = db.Column(db.String(255), nullable=True)
    whatsapp = db.Column(db.String(20), nullable=True)

    plan = db.Column(db.Enum(StorePlan), default=StorePlan.TRIAL, nullable=False)
    subscription_fee = db.Column(db.Float, default=0.0, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=get_local_time)
    updated_at = db.Column(db.DateTime, onupdate=get_local_time)
    is_active = db.Column(db.Boolean, default=True)

    accounts = db.relationship('StoreAccount', back_populates='store')
    categories = db.relationship('StoreCategory', back_populates='store')

    def check_expiration(self):
        if self.expiration_date < get_local_time():
            self.is_active = False

    def __repr__(self):
        return f"<Store {self.name} - Plan: {self.plan.value}>"

