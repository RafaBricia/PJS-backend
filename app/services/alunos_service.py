from app.firebase_config import db

def listar_alunos():
    alunos = db.collection("alunos").stream()
    return [u.to_dict() for u in alunos]

def criar_aluno(dados):
    doc_ref = db.collection("alunos").document()
    doc_ref.set({
        "nome": dados.get("nome"),
        "numeroOAB": dados.get("numeroOAB"),
        "codigo": dados.get("codigo"),
        "senha": dados.get("senha"),
        "email": dados.get("email"),
        "role": dados.get("role")
        })
    return {"id": doc_ref.id, **dados}


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

