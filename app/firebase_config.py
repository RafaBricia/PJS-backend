import firebase_admin
from firebase_admin import credentials, firestore
import os

CAMINHO_CHAVE = os.path.join(
    os.path.dirname(__file__),
    "pjsimulador-firebase-adminsdk-fbsvc-39df483558.json"  # coloque o arquivo JSON aqui dentro da pasta app
)

if not firebase_admin._apps:
    cred = credentials.Certificate(CAMINHO_CHAVE)
    firebase_admin.initialize_app(cred)

db = firestore.client()
