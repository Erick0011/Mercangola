from app.extensions import db
from .user import User, UserRole

class StoreAccount(User):
    __tablename__ = 'store_accounts'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    is_owner = db.Column(db.Boolean, default=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    position = db.Column(db.String(100), nullable=True)  # Ex: gerente, caixa, técnico

    store = db.relationship("Store", backref="accounts")

    __mapper_args__ = {
        'polymorphic_identity': UserRole.STORE_OWNER,
    }

    def __repr__(self):
        return f"<StoreAccount {self.email} - Owner: {self.is_owner}>"
