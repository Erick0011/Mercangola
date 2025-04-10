from app.services import get_local_time
from app.extensions import db
from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UserRole(Enum):
    ADMIN = "admin"
    STORE_OWNER = "store_owner"
    CLIENT = "client"

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)

    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)

    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=get_local_time())
    updated_at = db.Column(db.DateTime, onupdate=get_local_time())
    last_seen = db.Column(db.DateTime, default=get_local_time())

    def set_password(self, password):
        """Gera hash da senha"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica a senha"""
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"<User {self.email} - {self.role}>"
