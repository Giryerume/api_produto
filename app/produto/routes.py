from flask import jsonify, request
from flask_jwt_extended import jwt_required
from .. import db
from . import produto_bp
from .models import Produto

@produto_bp.route('/produtos', methods=['GET'])
@jwt_required()
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.serializar() for produto in produtos])

@produto_bp.route('/produtos/<int:id>', methods=['GET'])
@jwt_required()
def get_produto(id):
    produto = Produto.query.get_or_404(id)
    return jsonify(produto.serializar())

@produto_bp.route('/produtos', methods=['POST'])
@jwt_required()
def create_produto():
    data = request.json
    produto = Produto(nome=data['nome'], descricao=data['descricao'], preco=data['preco'])
    db.session.add(produto)
    db.session.commit()
    return jsonify({'message': 'Produto criado com sucesso!'}), 201

@produto_bp.route('/produtos/<int:id>', methods=['PUT'])
@jwt_required()
def update_produto(id):
    produto = Produto.query.get_or_404(id)
    data = request.json
    produto.nome = data['nome']
    produto.descricao = data['descricao']
    produto.preco = data['preco']
    db.session.commit()
    return jsonify({'message': 'Produto atualizado com sucesso!'})

@produto_bp.route('/produtos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto deletado com sucesso!'})
