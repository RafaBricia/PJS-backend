import random
import csv
from app.firebase_config import db
from io import StringIO

def listar_alunos():
    alunos = db.collection("alunos").stream()
    return [u.to_dict() for u in alunos]

def criar_alunos_lote(csv_file):
    alunos_ref = db.collection("alunos")
    criados = []
    falhas = []

    arquivo = StringIO(csv_file.read().decode('utf-8'))
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        try:
            codigo = str(random.randint(100000, 999999))

            doc_ref = alunos_ref.add({
                "nome": linha.get("nome"),
                "matricula": linha.get("matricula"),
                "email": linha.get("email"),
                "senha": linha.get("senha"),
                "role": linha.get("role", "aluno"),
                "codigoEmpresa": linha.get("codigoEmpresa"),
                "funcionarioId": linha.get("funcionarioId"),
                "codigo": codigo
            })

            aluno_id = doc_ref[1].id
            alunos_ref.document(aluno_id).update({"id": aluno_id})

            criados.append({
                "id": aluno_id,
                "codigo": codigo,
                **linha
            })

        except Exception as e:
            falhas.append({"linha": linha, "erro": str(e)})

    return {
        "sucesso": len(criados),
        "falhas": falhas,
        "alunosCriados": criados
    }

def criar_aluno(dados):
    alunos_ref = db.collection("alunos")
    codigo = str(random.randint(100000, 999999))  # Gera código de 6 dígitos

    doc_ref = alunos_ref.add({
        "nome": dados.get("nome"),
        "codigoEmpresa": dados.get("codigoEmpresa"),
        "matricula": dados.get("matricula"),
        "codigo": codigo,
        "senha": dados.get("senha"),
        "email": dados.get("email"),
        "role": dados.get("role")
    })

    aluno_id = doc_ref[1].id
    alunos_ref.document(aluno_id).update({"id": aluno_id})
    return {"id": aluno_id, "codigo": codigo, **dados}

def obter_aluno_por_id(aluno_id):
    doc_ref = db.collection("alunos").document(aluno_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def atualizar_aluno(aluno_id, dados):
    doc_ref = db.collection("alunos").document(aluno_id)
    doc_ref.update(dados)
    return {"id": aluno_id, **dados}

def deletar_aluno(aluno_id):
    doc_ref = db.collection("alunos").document(aluno_id)
    doc_ref.delete()
    return True

