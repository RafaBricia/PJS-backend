from app.firebase_config import db

def listar_funcionarios():
    funcionarios = db.collection("funcionarios").stream()
    return [u.to_dict() for u in funcionarios]

def criar_funcionario(dados):
    doc_ref = db.collection("funcionarios").document()
    doc_ref.set({
        "nome": dados.get("nome"),
        "matricula": dados.get("matricula"),
        "senha": dados.get("senha"),
        "email": dados.get("email"),
        "role": dados.get("role")
        })
    return {"id": doc_ref.id, **dados}


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