from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha_hash = generate_password_hash(senha)

    def checar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
