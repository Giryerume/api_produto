import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuração do bando de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuração do JWT
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    db.init_app(app)
    jwt = JWTManager(app)

    from .usuario.routes import usuario_bp
    from .produto.routes import produto_bp
    app.register_blueprint(usuario_bp)
    app.register_blueprint(produto_bp)

    from .produto.models import Produto

    with app.app_context():
        db.create_all()  

    return app
