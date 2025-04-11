from app.extensions import db


class Category(db.Model):
  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  icon = db.Column(db.String(50))  # Ex: 'tv', 'book', etc.

  store_categories = db.relationship('StoreCategory', back_populates='category')


def seed_categories():
  categories_data = [
    {"name": "Eletrônicos", "icon": "tv"},
    {"name": "Roupas", "icon": "tshirt"},
    {"name": "Alimentos", "icon": "apple-alt"},
    {"name": "Livros", "icon": "book"},
    {"name": "Esportes", "icon": "football-ball"},
    {"name": "Móveis", "icon": "couch"},
    {"name": "Brinquedos", "icon": "puzzle-piece"},
    {"name": "Beleza", "icon": "spa"},
    {"name": "Ferramentas", "icon": "tools"},
    {"name": "Saúde", "icon": "heartbeat"},
    {"name": "Celulares", "icon": "mobile-alt"},
    {"name": "Computadores", "icon": "laptop"},
    {"name": "Games", "icon": "gamepad"},
    {"name": "Cozinha", "icon": "blender"},
    {"name": "Viagem", "icon": "plane"},
    {"name": "Música", "icon": "music"},
    {"name": "Jardim", "icon": "leaf"},
    {"name": "Autopeças", "icon": "car"},
    {"name": "Relógios", "icon": "clock"},
    {"name": "Joias", "icon": "gem"},
    {"name": "Pet Shop", "icon": "paw"},
    {"name": "Papelaria", "icon": "pen"},
    {"name": "Fotografia", "icon": "camera"},
    {"name": "Cinema", "icon": "film"},
    {"name": "Calçados", "icon": "shoe-prints"},
    {"name": "Decoração", "icon": "paint-roller"},
    {"name": "Educação", "icon": "graduation-cap"},
    {"name": "Bebidas", "icon": "wine-glass-alt"},
    {"name": "Energia", "icon": "bolt"},
    {"name": "Serviços", "icon": "handshake"},
    {"name": "Moda Masculina", "icon": "male"},
    {"name": "Moda Feminina", "icon": "female"},
    {"name": "Tecnologia", "icon": "microchip"},
    {"name": "Construção", "icon": "hard-hat"},
    {"name": "Artes", "icon": "palette"},
    {"name": "Fitness", "icon": "dumbbell"},
    {"name": "Imóveis", "icon": "home"},
    {"name": "Bolsas", "icon": "shopping-bag"},
    {"name": "Bicicletas", "icon": "bicycle"},
    {"name": "Instrumentos Musicais", "icon": "guitar"},
    {"name": "Roupa Íntima", "icon": "user-secret"},
    {"name": "Carnes", "icon": "drumstick-bite"},
    {"name": "Produtos Naturais", "icon": "seedling"},
    {"name": "Maternidade", "icon": "baby"},
    {"name": "Eventos", "icon": "calendar-alt"},
    {"name": "Outros", "icon": "question-circle"},
    {"name": "Telefones Fixos", "icon": "phone"},
    {"name": "Transporte", "icon": "truck"},
    {"name": "Serviços Digitais", "icon": "cloud"}
  ]

  for data in categories_data:
    category = Category(name=data["name"], icon=data["icon"])
    db.session.add(category)

  db.session.commit()
  print("Categorias adicionadas com sucesso!")

class StoreCategory(db.Model):
  __tablename__ = 'store_categories'

  id = db.Column(db.Integer, primary_key=True)
  store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
  tenant_id = db.Column(db.String(50), nullable=False)  # herdado da loja
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

  category = db.relationship('Category', back_populates='store_categories')
  store = db.relationship('Store', back_populates='categories')


