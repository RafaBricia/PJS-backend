from flask import Blueprint, jsonify, request
from app.services.empresa_service import *

empresas_bp = Blueprint("empresas", __name__)

@empresas_bp.route('/empresas', methods=['GET'])
def get_empresas():
    return jsonify(listar_empresas()), 200 

@empresas_bp.route('/empresas', methods=['POST'])
def post_empresa():
    data = request.get_json()
    novo = criar_empresa(data)
    return jsonify(novo), 201

@empresas_bp.route('/empresas/<empresa_id>', methods=['GET'])
def get_empresa(empresa_id):
    empresa = buscar_empresa_por_codigo(empresa_id)
    if empresa:
        return jsonify(empresa), 200
    else:
        return jsonify({"error": "empresa não encontrado"}), 404
    
@empresas_bp.route('/empresas/<empresa_id>', methods=['PUT'])
def put_empresa(empresa_id):
    data = request.get_json()
    atualizado = atualizar_empresa(empresa_id, data)
    return jsonify(atualizado), 200

@empresas_bp.route('/empresas/<empresa_id>', methods=['DELETE'])
def delete_empresa(empresa_id):
    deletar_empresa(empresa_id)
    return jsonify({"message": "empresa deletado com sucesso"}), 200
