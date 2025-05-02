from app.extensions import db

class StoreCategory(db.Model):
  __tablename__ = 'store_categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
  tenant_id = db.Column(db.String(50), nullable=False)  # herdado da loja



  store = db.relationship('Store', back_populates='categories')


