from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from .. import db
from . import usuario_bp
from .models import Usuario

@usuario_bp.route('/register', methods=['POST'])
def register():
    dados = request.get_json()
    nome = dados.get('nome')
    senha = dados.get('senha')

    if Usuario.query.filter_by(nome=nome).first():
        return jsonify({'message': 'Usuario ja existe'}), 400

    novo_usuario = Usuario(nome=nome, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado com sucesso'}), 201

@usuario_bp.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    nome = dados.get('nome')
    senha = dados.get('senha')

    usuario = Usuario.query.filter_by(nome=nome).first()

    if not usuario or not usuario.checar_senha(senha):
        return jsonify({'message': 'Credenciais invalidas'}), 401

    access_token = create_access_token(identity=usuario.id)
    refresh_token = create_refresh_token(identity=usuario.id)

    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

@usuario_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    usuario_atual = get_jwt_identity()
    novo_access_token = create_access_token(identity=usuario_atual)
    return jsonify(access_token=novo_access_token), 200
