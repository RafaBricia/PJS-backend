from flask import Blueprint, jsonify, request
from app.services.processos_service import listar_processos, criar_processo, obter_processo_por_id,atualizar_processo,deletar_processo

processos_bp = Blueprint("processos", __name__)

@processos_bp.route('/processos', methods=['GET'])
def get_processos():
    return jsonify(listar_processos()), 200

@processos_bp.route('/processos', methods=['POST'])
def post_processo():
    data = request.get_json()
    novo = criar_processo(data)
    return jsonify(novo), 201

@processos_bp.route('/processos/<processo_id>', methods=['GET'])
def get_processo(processo_id):
    processo = obter_processo_por_id(processo_id)
    if processo:
        return jsonify(processo), 200
    else:
        return jsonify({"error": "processo não encontrado"}), 404

@processos_bp.route('/processos/<processo_id>', methods=['PUT'])
def put_processo(processo_id):
    data = request.get_json()
    atualizado = atualizar_processo(processo_id, data)
    return jsonify(atualizado), 200

@processos_bp.route('/processos/<processo_id>', methods=['DELETE'])
def delete_processo(processo_id):
    deletar_processo(processo_id)
    return jsonify({"message": "processo deletado com sucesso"}), 200
