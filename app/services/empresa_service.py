from app.firebase_config import db
from datetime import datetime


def criar_empresa(dados):
    import random
    empresas_ref = db.collection("empresas")
    codigo = str(random.randint(1000, 9999))  # Código de 4 dígitos, ex: 1234

    empresa = {
        "nome": dados.get("nome"),
        "codigo": codigo,
        "logo_url": dados.get("logo_url"),
        "papel_fundo_url": dados.get("papel_fundo_url"),
        "cor_primaria": dados.get("cor_primaria"),
        "cor_secundaria": dados.get("cor_secundaria"),
        "data_criacao": dados.get("data_criacao") or datetime.utcnow().isoformat(),
    }

    doc_ref = empresas_ref.add(empresa)
    empresa_id = doc_ref[1].id
    empresas_ref.document(empresa_id).update({"id": empresa_id})
    return {"id": empresa_id, "codigo": codigo, **empresa}


def buscar_empresa_por_codigo(codigo):
    query = db.collection("empresas").where("codigo", "==", codigo).limit(1).get()
    if not query:
        return None
    doc = query[0]
    empresa = doc.to_dict()
    empresa["id"] = doc.id
    return empresa


def atualizar_empresa(empresa_id, dados):
    doc_ref = db.collection("empresas").document(empresa_id)
    doc_ref.update(dados)
    empresa = doc_ref.get().to_dict()
    return {"id": empresa_id, **empresa}


def deletar_empresa(empresa_id):
    db.collection("empresas").document(empresa_id).delete()
    return True


def listar_empresas():
    docs = db.collection("empresas").get()
    empresas = []
    for doc in docs:
        empresa = doc.to_dict()
        empresa["id"] = doc.id
        empresas.append(empresa)
    return empresas
