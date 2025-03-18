from flask import Flask
from app.extensions import db
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa banco de dados
    db.init_app(app)

    # Importa as rotas
    from app.routes import public, dashboard, store, admin

    app.register_blueprint(public.bp)
    app.register_blueprint(dashboard.bp, url_prefix="/dashboard")
    app.register_blueprint(store.bp, url_prefix="/store")
    app.register_blueprint(admin.bp, url_prefix="/admin")


    return app
