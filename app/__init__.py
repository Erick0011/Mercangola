from flask import Flask
from app.extensions import db, login_manager
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa banco de dados e LoginManager
    db.init_app(app)
    login_manager.init_app(app)

    # Importa os modelos
    from app.models import Store, User, cart, analytics, category, product, review, customization, storeAccount, admin, client
    # Função para carregar o usuário pelo ID
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Importa as rotas
    from app.routes import public, dashboard, store, admin

    app.register_blueprint(public.bp)
    app.register_blueprint(dashboard.bp, url_prefix="/dashboard")
    app.register_blueprint(store.bp, url_prefix="/store")
    app.register_blueprint(admin.bp, url_prefix="/admin")


    return app
