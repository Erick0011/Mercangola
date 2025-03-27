from app.extensions import db
from datetime import datetime, timezone



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

    # Controle
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)

    # Relacionamento com o usuário
    owner = db.relationship('User', backref=db.backref('stores', lazy=True))

    def __repr__(self):
        return f"<Store {self.name}>"
