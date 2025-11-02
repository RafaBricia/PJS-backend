from app.firebase_config import db

def criar_processo(dados):
    """Cria um novo processo, aceitando lista de alunos."""
    doc_ref = db.collection("processos").document()

    alunos = dados.get("alunos")
    if not isinstance(alunos, list):
        alunos = [alunos] if alunos else [] 

    dados_processo = {
        "nomeProcesso": dados.get("nomeProcesso"),
        "dataInicial": dados.get("dataInicial"),
        "dataFinal": dados.get("dataFinal"),
        "juizResponsavel": dados.get("juizResponsavel"),
        "status": dados.get("status"),
        "descricao": dados.get("descricao"),
        "documento": dados.get("documento"),
        "alunos": alunos, 
        "tipoProcesso": dados.get("tipoProcesso")
    }

    doc_ref.set(dados_processo)
    return {"id": doc_ref.id, **dados_processo}


def atualizar_processo(processo_id, dados):
    """Atualiza um processo existente, garantindo lista em 'alunos'."""
    if "alunos" in dados and not isinstance(dados["alunos"], list):
        dados["alunos"] = [dados["alunos"]] if dados["alunos"] else []

    doc_ref = db.collection("processos").document(processo_id)
    doc_ref.update(dados)
    return {"id": processo_id, **dados}

def listar_processos():
    processos = db.collection("processos").stream()
    return [u.to_dict() for u in processos]

def obter_processo_por_id(processo_id):
    doc_ref = db.collection("processos").document(processo_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def deletar_processo(processo_id):
    doc_ref = db.collection("processos").document(processo_id)
    doc_ref.delete()
    return True