from app.firebase_config import db
import random
import csv
from io import StringIO

def criar_funcionarios_lote(csv_file):
    funcionarios_ref = db.collection("funcionarios")

    criados = []
    falhas = []

    conteudo = csv_file.read().decode("utf-8")
    arquivo = StringIO(conteudo)

    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        try:
            funcionario_data = {
                "nome": linha.get("nome"),
                "email": linha.get("email"),
                "senha": linha.get("senha"),
                "role": linha.get("role", "funcionario"),
                "codigoEmpresa": linha.get("codigoEmpresa"),
                "numeroOAB": linha.get("numeroOAB")
            }

            doc_ref = funcionarios_ref.add(funcionario_data)
            funcionario_id = doc_ref[1].id

            funcionarios_ref.document(funcionario_id).update({"id": funcionario_id})

            criados.append({
                "id": funcionario_id,
                **funcionario_data
            })

        except Exception as e:
            falhas.append({
                "linha": linha,
                "erro": str(e)
            })

    return {
        "sucesso": len(criados),
        "falhas": falhas,
        "funcionariosCriados": criados
    }


def listar_funcionarios():
    funcionarios = db.collection("funcionarios").stream()
    return [u.to_dict() for u in funcionarios]

def criar_funcionario(dados):
    funcionarios_ref = db.collection("funcionarios")

    doc_ref = funcionarios_ref.add({
        "nome": dados.get("nome"),
        "codigoEmpresa": dados.get("codigoEmpresa"),
        "senha": dados.get("senha"),
        "email": dados.get("email"),
        "role": dados.get("role"),
        "numeroOAB": dados.get("numeroOAB")
    })

    funcionario_id = doc_ref[1].id
    funcionarios_ref.document(funcionario_id).update({"id": funcionario_id})
    return {"id": funcionario_id, **dados}


def obter_funcionario_por_id(funcionario_id):
    doc_ref = db.collection("funcionarios").document(funcionario_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def atualizar_funcionario(funcionario_id, dados):
    doc_ref = db.collection("funcionarios").document(funcionario_id)
    doc_ref.update(dados)
    return {"id": funcionario_id, **dados}

def deletar_funcionario(funcionario_id):
    doc_ref = db.collection("funcionarios").document(funcionario_id)
    doc_ref.delete()
    return True