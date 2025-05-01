from app.extensions import db
from .user import User, UserRole
from enum import Enum

class StoreAccessLevel(Enum):
    OWNER = "owner"                      # dono da loja
    MANAGER = "manager"                  # gerente
    ASSISTANT_MANAGER = "assistant_manager"  # assistente do gerente


class StoreAccount(User):
    __tablename__ = 'store_accounts'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    is_owner = db.Column(db.Boolean, default=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    store_access_level = db.Column(db.Enum(StoreAccessLevel), nullable=True)

    store = db.relationship("Store", backref="accounts")

    __mapper_args__ = {
        'polymorphic_identity': UserRole.STORE_OWNER,
    }

    def __repr__(self):
        return f"<StoreAccount {self.email} - Owner: {self.is_owner}>"
