from app.extensions import db
from .user import User, UserRole

class Client(User):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    birthday = db.Column(db.Date, nullable=True)
    preferences = db.Column(db.JSON, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': UserRole.CLIENT,
    }

    def __repr__(self):
        return f"<Client {self.email}>"
