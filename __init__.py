# app/__init__.py
from flask import Flask
from app.routes.alunos_routes import *
from app.routes.funcionarios_routes import *
from app.routes.mensagens_routes import *
from app.routes.auth_routes import *
from app.routes.processos_routes import *
from app.routes.empresas_routes import *


def create_app():
    app = Flask(__name__)

    app.register_blueprint(alunos_bp, url_prefix="/api")
    app.register_blueprint(funcionarios_bp, url_prefix="/api")
    app.register_blueprint(mensagens_bp, url_prefix="/api")
    app.register_blueprint(processos_bp, url_prefix="/api")
    app.register_blueprint(auth_bd, url_prefix="/api")
    app.register_blueprint(empresas_bp, url_prefix="/api")

    @app.route('/')
    def home():
        return "Servidor Flask + Firebase está rodando!"

    return app
