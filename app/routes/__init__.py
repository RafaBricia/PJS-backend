from flask import Flask
from flask_cors import CORS
from .funcionarios_routes import funcionarios_bp
from .alunos_routes import alunos_bp
from .empresas_routes import empresas_bp
from .processos_routes import processos_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(funcionarios_bp, url_prefix="/api/funcionarios")
    app.register_blueprint(alunos_bp, url_prefix="/api/alunos")
    app.register_blueprint(empresas_bp, url_prefix="/api/empresas")
    app.register_blueprint(processos_bp, url_prefix="/api/processos")

    return app
