from functools import wraps
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.config import Config
from app.extensions import db
from app.models.servico_model import Servico
from app.routes.agendamento_routes import agendamento_bp
from app.routes.cliente_routes import cliente_bp
from app.routes.servico_routes import servico_bp


def create_app():
    app = Flask(
        __name__, template_folder="../templates", static_folder="../static"
    )

    # 1. IMPORTAÇÃO DE CONFIGURAÇÕES E CHAVES DE SEGURANÇA
    app.config.from_object(Config)

    # Chave secreta obrigatória para o Flask assinar a sessão digitalmente
    app.secret_key = "chave_secreta_super_segura_do_salao_santana"

    # Credenciais seguras do administrador (Senha atual: "123")
    ADMIN_USUARIO = "admin"
    ADMIN_SENHA_HASH = generate_password_hash("123")

    # 2. CONEXÃO COM O BANCO DE DADOS E BLUEPRINTS
    db.init_app(app)

    app.register_blueprint(cliente_bp)
    app.register_blueprint(servico_bp)
    app.register_blueprint(agendamento_bp)

    # =====================================================================
    # 3. TRAVA DE SEGURANÇA (DECORADOR DE PROTEÇÃO DO PAINEL)
    # =====================================================================
    def admin_requerido(f):
        @wraps(f)
        def rota_protegida(*args, **kwargs):
            # Se não existir sessão ativa para o admin, barra a requisição
            if "admin_logado" not in session:
                # Se for requisição de JavaScript (fetch/json), devolve erro 401
                if request.is_json or request.path.startswith("/api/"):
                    return (
                        jsonify(
                            {
                                "erro": (
                                    "Acesso não autorizado. Faça login"
                                    " primeiro."
                                )
                            }
                        ),
                        401,
                    )
                # Se for acesso pelo navegador, redireciona para a tela de login
                return redirect("/admin")
            return f(*args, **kwargs)

        return rota_protegida

    # =====================================================================
    # 4. ROTAS PÚBLICAS (CLIENTES E VISITANTES)
    # =====================================================================
    @app.route("/")
    def public_home():
        return render_template("public/index.html")

    @app.route("/agendar")
    def agendar_page():
        return render_template("public/agendar.html")

    @app.route("/meu-historico")
    def pagina_historico():
        return render_template("public/historico.html")

    # =====================================================================
    # 5. ROTAS DE AUTENTICAÇÃO (LOGIN E LOGOUT)
    # =====================================================================
    @app.route("/admin")
    def admin_login():
        # Se o admin já estiver logado, entra direto no painel
        if "admin_logado" in session:
            return redirect("/admin/dashboard")
        return render_template("admin/login.html")

    @app.route("/login", methods=["POST"])
    def fazer_login():
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Dados inválidos."}), 400

        usuario = dados.get("usuario")
        senha = dados.get("senha")

        # Verifica usuário e confere o hash da senha
        if usuario == ADMIN_USUARIO and check_password_hash(
            ADMIN_SENHA_HASH, senha
        ):
            session["admin_logado"] = True
            session["usuario"] = usuario
            return jsonify({"mensagem": "Login bem-sucedido!"}), 200
        else:
            return jsonify({"erro": "Usuário ou senha incorretos."}), 401

    @app.route("/logout")
    def fazer_logout():
        session.clear()
        return redirect("/admin")

    # =====================================================================
    # 6. ROTAS PROTEGIDAS DO PAINEL ADMIN (@admin_requerido)
    # =====================================================================
    @app.route("/admin/dashboard")
    @admin_requerido
    def admin_dashboard():
        return render_template("admin/dashboard.html")

    @app.route("/admin/clientes")
    @admin_requerido
    def admin_clientes():
        return render_template("admin/clientes.html")

    @app.route("/admin/servicos")
    @admin_requerido
    def admin_servicos():
        return render_template("admin/servicos.html")

    @app.route("/admin/agendamentos")
    @admin_requerido
    def admin_agendamentos():
        return render_template("admin/agendamentos.html")

    # =====================================================================
    # 7. CARREGAMENTO AUTOMÁTICO DE SERVIÇOS INICIAIS NO BD
    # =====================================================================
    with app.app_context():
        # Verifica se está vazio, senão cria
        db.create_all()

        if Servico.query.count() == 0:
            servicos = [
                Servico(nome="Corte de Cabelo", preco=40, duracao=60),
                Servico(nome="Sobrancelha", preco=25, duracao=30),
                Servico(nome="Progressiva", preco=150, duracao=180),
                Servico(nome="Tintura", preco=120, duracao=120),
                Servico(nome="Unha", preco=35, duracao=60),
                Servico(
                    nome="Maquiagem Completa", preco=100, duracao=90
                ),
            ]

            db.session.add_all(servicos)
            db.session.commit()
            print("Serviços cadastrados automaticamente!")

    return app