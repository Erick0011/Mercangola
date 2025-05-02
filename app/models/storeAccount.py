from app.extensions import db
from .user import User, UserRole
from enum import Enum

class StoreAccessLevel(Enum):
    OWNER = "owner"                      # dono da loja
    MANAGER = "manager"                  # gerente
    ASSISTANT_MANAGER = "assistant_manager"  # assistente do gerente

STORE_ACCESS_LEVEL_LABELS = {
    StoreAccessLevel.OWNER: "Dono da loja",
    StoreAccessLevel.MANAGER: "Gerente",
    StoreAccessLevel.ASSISTANT_MANAGER: "Assistente do gerente"
}

class StoreAccount(User):
    __tablename__ = 'store_accounts'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    store_access_level = db.Column(db.Enum(StoreAccessLevel), nullable=False)

    store = db.relationship("Store", back_populates="accounts")

    __mapper_args__ = {
        'polymorphic_identity': UserRole.STORE_OWNER,
    }

    @property
    def access_level_label(self):
        return STORE_ACCESS_LEVEL_LABELS.get(self.store_access_level, "Desconhecido")

    def __repr__(self):
        return f"<StoreAccount {self.email} - {self.store_access_level.value}>"
