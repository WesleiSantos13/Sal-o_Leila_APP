from flask import Blueprint
from app.controllers.servico_controller import (
    criar_servico,
    listar_servicos,
    deletar_servico,
    atualizar_servico
)

servico_bp = Blueprint('servico', __name__)

@servico_bp.route('/servicos', methods=['POST'])
def rota_criar_servico():
    """Chama o controlador para cadastrar um novo serviço no salão."""
    return criar_servico()

@servico_bp.route('/servicos', methods=['GET'])
def rota_listar_servicos():
    """Chama o controlador para listar todos os serviços disponíveis."""
    return listar_servicos()

@servico_bp.route("/servicos/<int:id>", methods=["DELETE"])
def deletar_servico_route(id):
    """Chama o controlador para remover um serviço específico através do ID."""
    return deletar_servico(id)

@servico_bp.route("/servicos/<int:id>", methods=["PUT"])
def atualizar_servico_route(id):
    """Chama o controlador para atualizar as informações de um serviço existente."""
    return atualizar_servico(id)