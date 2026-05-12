from flask import Flask, render_template

from app.config import Config
from app.extensions import db

from app.models.servico_model import Servico
from app.routes.cliente_routes import cliente_bp
from app.routes.servico_routes import servico_bp
from app.routes.agendamento_routes import agendamento_bp


def create_app():

    app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(cliente_bp)
    app.register_blueprint(servico_bp)
    app.register_blueprint(agendamento_bp)


    @app.route("/")
    def public_home():
        return render_template("public/index.html")


    @app.route("/agendar")
    def agendar_page():
        return render_template("public/agendar.html")


    @app.route("/admin")
    def admin_login():
        return render_template("admin/login.html")


    @app.route("/admin/dashboard")
    def admin_dashboard():
        return render_template("admin/dashboard.html")


    @app.route("/admin/clientes")
    def admin_clientes():
        return render_template("admin/clientes.html")


    @app.route("/admin/servicos")
    def admin_servicos():
        return render_template("admin/servicos.html")


    @app.route("/admin/agendamentos")
    def admin_agendamentos():
        return render_template("admin/agendamentos.html")
    
    @app.route('/meu-historico')
    def pagina_historico():
       return render_template('public/historico.html')



# Cadastrando só para facilitar testes
    with app.app_context():

        db.create_all()

        if Servico.query.count() == 0:

            servicos = [

                Servico(
                    nome="Corte de Cabelo",
                    preco=40,
                    duracao=60
                ),

                Servico(
                    nome="Sobrancelha",
                    preco=25,
                    duracao=30
                ),

                Servico(
                    nome="Progressiva",
                    preco=150,
                    duracao=180
                ),

                Servico(
                    nome="Tintura",
                    preco=120,
                    duracao=120
                ),

                Servico(
                    nome="Unha",
                    preco=35,
                    duracao=60
                ),

                Servico(
                    nome="Maquiagem Completa",
                    preco=100,
                    duracao=90
                )
            ]

            db.session.add_all(servicos)

            db.session.commit()

            print("Serviços cadastrados automaticamente!")



    return app