from app.firebase_config import db

def _get_collection(processo_id=None):
    if processo_id:
        return db.collection("processos").document(processo_id).collection("mensagens")
    return db.collection("mensagens")


def listar_mensagens(processo_id=None):
    mensagens_ref = _get_collection(processo_id)
    mensagens = mensagens_ref.stream()
    return [{**m.to_dict(), "id": m.id} for m in mensagens]


def criar_mensagem(dados, processo_id=None, garantir_lista_dest=True):
    import random
    mensagens_ref = _get_collection(processo_id)
    codigo = str(random.randint(100000, 999999))

    doc_ref = mensagens_ref.add({})
    mensagem_id = doc_ref[1].id

    destinatario = dados.get("destinatario", [])
    if garantir_lista_dest:
        if isinstance(destinatario, list):
            destinatarios = destinatario
        else:
            destinatarios = [destinatario] if destinatario else []
    else:
        destinatarios = destinatario

    dados_mensagem = {
        "codigo": codigo,
        "autor": dados.get("autor"),
        "conteudo": dados.get("conteudo"),
        "dataEnvio": dados.get("dataEnvio"),
        "tipo": dados.get("tipo"),
        "anexos": dados.get("anexos", []),
        "destinatario": destinatarios,
        "processoId": processo_id
    }

    mensagens_ref.document(mensagem_id).set({**dados_mensagem, "id": mensagem_id})
    return {"id": mensagem_id, "codigo": codigo, **dados_mensagem}



def obter_mensagem_por_id(mensagem_id, processo_id=None):
    mensagens_ref = _get_collection(processo_id)
    doc_ref = mensagens_ref.document(mensagem_id)
    doc = doc_ref.get()
    if doc.exists:
        return {"id": doc.id, **doc.to_dict()}
    return None


def atualizar_mensagem(mensagem_id, dados, processo_id=None, garantir_lista_dest=True):
    if "destinatario" in dados and garantir_lista_dest:
        dest = dados["destinatario"]
        if not isinstance(dest, list):
            dados["destinatario"] = [dest] if dest else []

    mensagens_ref = _get_collection(processo_id)
    doc_ref = mensagens_ref.document(mensagem_id)
    doc_ref.update(dados)
    return {"id": mensagem_id, **dados}


def deletar_mensagem(mensagem_id, processo_id=None):
    mensagens_ref = _get_collection(processo_id)
    doc_ref = mensagens_ref.document(mensagem_id)
    doc_ref.delete()
    return True
