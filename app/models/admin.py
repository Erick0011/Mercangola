from app.extensions import db
from .user import User, UserRole

class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    system_access_level = db.Column(db.String(50), nullable=True)  # Exemplo de campo específico

    __mapper_args__ = {
        'polymorphic_identity': UserRole.ADMIN,
    }

    def __repr__(self):
        return f"<Admin {self.email}>"
