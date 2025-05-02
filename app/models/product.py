from app.extensions import db
from app.services import get_local_time

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)  # <- Aqui
    store = db.relationship("Store", backref="products")
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer, default=0)
    sku = db.Column(db.String(100), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=get_local_time)
    updated_at = db.Column(db.DateTime, default=get_local_time, onupdate=get_local_time())

    # Categoria
    store_category_id = db.Column(db.Integer, db.ForeignKey('store_categories.id'))
    store_category = db.relationship("StoreCategory", backref="products")

    # Produto pai (se for variação)
    parent_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    variations = db.relationship("Product", backref=db.backref('parent', remote_side='Product.id'))

    # Relações
    media = db.relationship("ProductMedia", backref="product", cascade="all, delete")
    reviews = db.relationship("Review", backref="product", cascade="all, delete")
    favorites = db.relationship("Favorite", backref="product", cascade="all, delete")
    views = db.relationship("ProductView", backref="product", cascade="all, delete")
    attributes = db.relationship("ProductAttribute", backref="product", cascade="all, delete")
    tags = db.relationship("ProductTag", backref="product", cascade="all, delete")

class ProductAttribute(db.Model):
    __tablename__ = 'product_attributes'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)  # Ex: Cor, Tamanho, País de origem
    value = db.Column(db.String(255), nullable=False) # Ex: Azul, M, Angola

class ProductTag(db.Model):
    __tablename__ = 'product_tags'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False, index=True)



class ProductMedia(db.Model):
    __tablename__ = 'product_media'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    url = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(10))  # 'image' or 'video'
    order = db.Column(db.Integer, default=0)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=get_local_time)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    __table_args__ = (
        db.UniqueConstraint('product_id', 'user_id', name='unique_product_user_fav'),
    )


