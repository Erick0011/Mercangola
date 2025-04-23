from app import create_app
from app.extensions import db
from app.models.user import User, UserRole
from app.models import seed_categories

app = create_app()

with app.app_context():
    db.create_all()  # Cria todas as tabelas

    # Cria as categorias disponiveis - fix temporario
    seed_categories()

    # Verificar se já existem usuários para evitar duplicação
    if not User.query.first():
        users = [
            User(
                email="admin@example.com",
                name="Admin User",
                telefone="999999999",
                role=UserRole.ADMIN,
            ),
            User(
                email="store@example.com",
                name="Store Owner",
                telefone="888888888",
                role=UserRole.STORE_OWNER,
            ),
            User(
                email="client@example.com",
                name="Client User",
                telefone="777777777",
                role=UserRole.CLIENT,
            ),
        ]

        # Definir senha para cada usuário
        for user in users:
            user.set_password("12345")  # Senha será armazenada com hash
            db.session.add(user)

        db.session.commit()
        print("Banco de dados criado e usuários inseridos com sucesso!")

if __name__ == "__main__":
    app.run(debug=True)
