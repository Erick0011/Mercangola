import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Diretório base dos uploads
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app", "static", "uploads")

    # Definir subpastas para organização
    STORE_UPLOADS = os.path.join(UPLOAD_FOLDER, "stores")
    PROFILE_PICTURES = os.path.join(UPLOAD_FOLDER, "profile_pictures")

    # Tipos de arquivos permitidos
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

    # Criar diretórios automaticamente se não existirem
    for folder in [UPLOAD_FOLDER, STORE_UPLOADS, PROFILE_PICTURES]:
        os.makedirs(folder, exist_ok=True)
