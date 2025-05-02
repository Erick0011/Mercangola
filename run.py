from app import create_app
from app.extensions import db
from app.models.user import User, UserRole

app = create_app()

with app.app_context():
    db.create_all()  # Cria todas as tabelas



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

