from app.extensions import db
from app.services import get_local_time

class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    quantity = db.Column(db.Integer, default=1)
    added_at = db.Column(db.DateTime, default=get_local_time())

    processed = db.Column(db.Boolean, default=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    product = db.relationship("Product")
    user = db.relationship("User")

    __table_args__ = (
        db.UniqueConstraint('product_id', 'user_id', name='unique_cart_item'),
    )

class CartAbandonment(db.Model):
    __tablename__ = 'cart_abandonments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tenant_id = db.Column(db.String(50), nullable=False)
    abandoned_at = db.Column(db.DateTime, default=get_local_time)
    products = db.Column(db.Text)  # Lista dos produtos abandonados, pode ser armazenada como JSON ou texto

    user = db.relationship("User")