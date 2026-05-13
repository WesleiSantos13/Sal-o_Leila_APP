from flask import Blueprint
from app.controllers.cliente_controller import (
    criar_cliente,
    listar_clientes,
    deletar_cliente
)

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes', methods=['POST'])
def rota_criar_cliente():
    """Chama o controlador para processar a criação de um novo cliente."""
    return criar_cliente()

@cliente_bp.route('/clientes', methods=['GET'])
def rota_listar_clientes():
    """Chama o controlador para retornar a listagem de todos os clientes."""
    return listar_clientes()

@cliente_bp.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente_route(id):
    """Chama o controlador para realizar a exclusão de um cliente pelo ID."""
    return deletar_cliente(id)