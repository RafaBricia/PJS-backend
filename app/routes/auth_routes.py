from flask import Blueprint, jsonify, request
import csv
import io

auth_bd = Blueprint("auth", __name__)

@auth_bd.route('/login/root', methods=['POST'])
def login_root():
    """Login para Usuário Root (administrador do sistema)"""
    data = request.get_json()
    codigo = data.get("codigo")
    
    if not codigo:
        return jsonify({"error": "Código é obrigatório"}), 400
    
    
    return jsonify({
        "message": "Login root bem-sucedido",
        "tipo": "root"
    }), 200


@auth_bd.route('/login/funcionario', methods=['POST'])
def login_funcionario():
    """Login para Funcionário (com código e CNPJ ou senha)"""
    data = request.get_json()
    codigo = data.get("codigo")
    cnpj = data.get("cnpj")
    senha = data.get("senha")
    
    if not codigo:
        return jsonify({"error": "Código é obrigatório"}), 400
    
    if not cnpj and not senha:
        return jsonify({"error": "CNPJ ou senha é obrigatório"}), 400
   
    return jsonify({
        "message": "Login funcionário bem-sucedido",
        "tipo": "funcionario"
    }), 200


@auth_bd.route('/login/aluno', methods=['POST'])
def login_aluno():
    data = request.get_json()
    matricula = data.get("matricula")
    senha = data.get("senha")
    
    if not matricula or not senha:
        return jsonify({"error": "Matrícula e senha são obrigatórios"}), 400
    

    return jsonify({
        "message": "Login aluno bem-sucedido",
        "tipo": "aluno"
    }), 200


@auth_bd.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "Logout bem-sucedido"}), 200


@auth_bd.route('/register/aluno', methods=['POST'])
def register_aluno():
    """Registro de alunos através de arquivo CSV
    
    Formato esperado do CSV:
    matricula,nome,senha
    12345,João Silva,senha123
    67890,Maria Santos,senha456
    """
    
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Arquivo vazio"}), 400
    
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Apenas arquivos CSV são permitidos"}), 400
    
    try:
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_reader = csv.DictReader(stream)
        
        alunos_adicionados = []
        alunos_erros = []
        
        for row in csv_reader:
            matricula = row.get('matricula', '').strip()
            nome = row.get('nome', '').strip()
            senha = row.get('senha', '').strip()
            
            if not matricula or not nome or not senha:
                alunos_erros.append({
                    "matricula": matricula,
                    "erro": "Dados incompletos"
                })
                continue
            
            alunos_adicionados.append({
                "matricula": matricula,
                "nome": nome
            })
        
        return jsonify({
            "message": f"{len(alunos_adicionados)} alunos registrados com sucesso!",
            "alunos_adicionados": alunos_adicionados,
            "alunos_erros": alunos_erros
        }), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro ao processar CSV: {str(e)}"}), 500