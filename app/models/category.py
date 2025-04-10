from app.extensions import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.String(50), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(50))  # FontAwesome icon name

categories = [
  { "nome": "Eletrônicos", "icon": "tv" },
  { "nome": "Roupas", "icon": "tshirt" },
  { "nome": "Alimentos", "icon": "apple-alt" },
  { "nome": "Livros", "icon": "book" },
  { "nome": "Esportes", "icon": "football-ball" },
  { "nome": "Móveis", "icon": "couch" },
  { "nome": "Brinquedos", "icon": "puzzle-piece" },
  { "nome": "Beleza", "icon": "spa" },
  { "nome": "Ferramentas", "icon": "tools" },
  { "nome": "Saúde", "icon": "heartbeat" },
  { "nome": "Celulares", "icon": "mobile-alt" },
  { "nome": "Computadores", "icon": "laptop" },
  { "nome": "Games", "icon": "gamepad" },
  { "nome": "Cozinha", "icon": "blender" },
  { "nome": "Viagem", "icon": "plane" },
  { "nome": "Música", "icon": "music" },
  { "nome": "Jardim", "icon": "leaf" },
  { "nome": "Autopeças", "icon": "car" },
  { "nome": "Relógios", "icon": "clock" },
  { "nome": "Joias", "icon": "gem" },
  { "nome": "Pet Shop", "icon": "paw" },
  { "nome": "Papelaria", "icon": "pen" },
  { "nome": "Fotografia", "icon": "camera" },
  { "nome": "Cinema", "icon": "film" },
  { "nome": "Calçados", "icon": "shoe-prints" },
  { "nome": "Decoração", "icon": "paint-roller" },
  { "nome": "Educação", "icon": "graduation-cap" },
  { "nome": "Bebidas", "icon": "wine-glass-alt" },
  { "nome": "Energia", "icon": "bolt" },
  { "nome": "Serviços", "icon": "handshake" },
  { "nome": "Moda Masculina", "icon": "male" },
  { "nome": "Moda Feminina", "icon": "female" },
  { "nome": "Tecnologia", "icon": "microchip" },
  { "nome": "Construção", "icon": "hard-hat" },
  { "nome": "Artes", "icon": "palette" },
  { "nome": "Fitness", "icon": "dumbbell" },
  { "nome": "Imóveis", "icon": "home" },
  { "nome": "Bolsas", "icon": "shopping-bag" },
  { "nome": "Bicicletas", "icon": "bicycle" },
  { "nome": "Instrumentos Musicais", "icon": "guitar" },
  { "nome": "Roupa Íntima", "icon": "user-secret" },
  { "nome": "Carnes", "icon": "drumstick-bite" },
  { "nome": "Produtos Naturais", "icon": "seedling" },
  { "nome": "Maternidade", "icon": "baby" },
  { "nome": "Eventos", "icon": "calendar-alt" },
  { "nome": "Outros", "icon": "question-circle" },
  { "nome": "Telefones Fixos", "icon": "phone" },
  { "nome": "Transporte", "icon": "truck" },
  { "nome": "Serviços Digitais", "icon": "cloud" }
]
