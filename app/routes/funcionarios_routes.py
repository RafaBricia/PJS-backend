from flask import Blueprint, jsonify, request
from app.services.funcionarios_service import listar_funcionarios, criar_funcionario, obter_funcionario_por_id,atualizar_funcionario,deletar_funcionario,criar_funcionarios_lote

funcionarios_bp = Blueprint("funcionarios", __name__)

@funcionarios_bp.route("/funcionarios/lote", methods=["POST"])
def upload_funcionarios_csv():
    if "file" not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400

    arquivo = request.files["file"]

    if arquivo.filename == "":
        return jsonify({"erro": "Nome de arquivo inválido"}), 400

    resultado = criar_funcionarios_lote(arquivo)
    return jsonify(resultado), 201


@funcionarios_bp.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    return jsonify(listar_funcionarios()), 200

@funcionarios_bp.route('/funcionarios', methods=['POST'])
def post_funcionario():
    data = request.get_json()
    novo = criar_funcionario(data)
    return jsonify(novo), 201

@funcionarios_bp.route('/funcionarios/<funcionario_id>', methods=['GET'])
def get_funcionario(funcionario_id):
    funcionario = obter_funcionario_por_id(funcionario_id)
    if funcionario:
        return jsonify(funcionario), 200
    else:
        return jsonify({"error": "funcionario não encontrado"}), 404

@funcionarios_bp.route('/funcionarios/<funcionario_id>', methods=['PUT'])
def put_funcionario(funcionario_id):
    data = request.get_json()
    atualizado = atualizar_funcionario(funcionario_id, data)
    return jsonify(atualizado), 200

@funcionarios_bp.route('/funcionarios/<funcionario_id>', methods=['DELETE'])
def delete_funcionario(funcionario_id):
    deletar_funcionario(funcionario_id)
    return jsonify({"message": "funcionario deletado com sucesso"}), 200
