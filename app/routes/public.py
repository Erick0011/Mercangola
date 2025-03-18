from flask import Blueprint

bp = Blueprint('public', __name__)

@bp.route('/')
def home():
    return "Página Inicial - Explicação do Serviço"

@bp.route('/login')
def login():
    return "Página de Login"

@bp.route('/register')
def register():
    return "Página de Cadastro de Lojista"

