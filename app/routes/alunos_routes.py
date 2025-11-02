from flask import Blueprint, request, jsonify
from app.services.alunos_service import listar_alunos, criar_aluno, obter_aluno_por_id,atualizar_aluno,deletar_aluno

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos()), 200

@alunos_bp.route('/alunos', methods=['POST'])
def post_aluno():
    data = request.get_json()
    novo = criar_aluno(data)
    return jsonify(novo), 201

@alunos_bp.route('/alunos/<aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = obter_aluno_por_id(aluno_id)
    if aluno:
        return jsonify(aluno), 200
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404

@alunos_bp.route('/alunos/<aluno_id>', methods=['PUT'])
def put_aluno(aluno_id):
    data = request.get_json()
    atualizado = atualizar_aluno(aluno_id, data)
    return jsonify(atualizado), 200

@alunos_bp.route('/alunos/<aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    deletar_aluno(aluno_id)
    return jsonify({"message": "Aluno deletado com sucesso"}), 200
