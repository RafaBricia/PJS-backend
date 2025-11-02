from flask import Blueprint, request, jsonify
from app.services.mensagens_service import listar_mensagens, criar_mensagem, obter_mensagem_por_id,atualizar_mensagem,deletar_mensagem

mensagens_bp = Blueprint('mensagens', __name__)

@mensagens_bp.route('/mensagens', methods=['GET'])
def get_mensagens():
    return jsonify(listar_mensagens()), 200

@mensagens_bp.route('/mensagens', methods=['POST'])
def post_mensagem():
    data = request.get_json()
    novo = criar_mensagem(data)
    return jsonify(novo), 201

@mensagens_bp.route('/mensagens/<mensagem_id>', methods=['GET'])
def get_mensagem(mensagem_id):
    mensagem = obter_mensagem_por_id(mensagem_id)
    if mensagem:
        return jsonify(mensagem), 200
    else:
        return jsonify({"error": "mensagem não encontrado"}), 404

@mensagens_bp.route('/mensagens/<mensagem_id>', methods=['PUT'])
def put_mensagem(mensagem_id):
    data = request.get_json()
    atualizado = atualizar_mensagem(mensagem_id, data)
    return jsonify(atualizado), 200

@mensagens_bp.route('/mensagens/<mensagem_id>', methods=['DELETE'])
def delete_mensagem(mensagem_id):
    deletar_mensagem(mensagem_id)
    return jsonify({"message": "mensagem deletado com sucesso"}), 200
