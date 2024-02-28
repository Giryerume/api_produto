from .. import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    preco = db.Column(db.Float, nullable=False)

    def serializar(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco
        }
