from app.extensions import db
from .user import User, UserRole
from enum import Enum

class SystemAccessLevel(Enum):
    SUPER_ADMIN = "super_admin"       # acesso total
    ADMIN = "admin"                   # acesso amplo, mas limitado
    MODERATOR = "moderator"          # pode ver e editar, mas sem ações críticas
    VIEWER = "viewer"                # apenas leitura


class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    system_access_level = db.Column(db.Enum(SystemAccessLevel), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': UserRole.ADMIN,
    }

    def __repr__(self):
        return f"<Admin {self.email}>"
