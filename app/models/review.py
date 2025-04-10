from app.extensions import db
from app.services import get_local_time

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    rating = db.Column(db.Integer)  # Nota da avaliação
    comment = db.Column(db.Text)  # Comentário da avaliação
    created_at = db.Column(db.DateTime, default=get_local_time())  # Quando a avaliação foi criada

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))  # Produto relacionado
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Usuário que fez a avaliação

    # Relacionamento com a tabela de mídia (fotos ou vídeos)
    media = db.relationship("ReviewMedia", backref="review", cascade="all, delete")

class ReviewMedia(db.Model):
    __tablename__ = 'review_media'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    url = db.Column(db.Text, nullable=False)  # URL da foto ou vídeo
    type = db.Column(db.String(10))  # Tipo de mídia: 'image' ou 'video'
    order = db.Column(db.Integer, default=0)  # Ordem em que as fotos são exibidas

    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))  # Relacionamento com a avaliação


    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)