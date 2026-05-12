from flask import Blueprint
from app.controllers.agendamento_controller import (
    criar_agendamento,
    listar_agendamentos,
    atualizar_status,
    deletar_agendamento,
    buscar_historico_cliente,
    alterar_data_agendamento
)

agendamento_bp = Blueprint('agendamento', __name__)

@agendamento_bp.route('/agendamentos', methods=['POST'])
def rota_criar_agendamento():
    """Endpoint para criar um novo agendamento."""
    return criar_agendamento()

@agendamento_bp.route('/agendamentos', methods=['GET'])
def rota_listar_agendamentos():
    """Endpoint para listar todos os agendamentos."""
    return listar_agendamentos()

@agendamento_bp.route('/agendamentos/<int:id>', methods=['PUT'])
def rota_atualizar_status(id):
    """Endpoint para atualizar o status de um agendamento específico."""
    return atualizar_status(id)

@agendamento_bp.route('/agendamentos/<int:id>', methods=['DELETE'])
def rota_deletar_agendamento(id):
    """Endpoint para remover um agendamento do sistema."""
    return deletar_agendamento(id)

@agendamento_bp.route('/api/historico', methods=['GET'])
def rota_buscar_historico():
    """Endpoint para buscar o histórico de agendamentos via e-mail."""
    return buscar_historico_cliente()

@agendamento_bp.route('/agendamentos/<int:id>/data', methods=['PUT'])
def rota_alterar_data(id):
    """Endpoint exclusivo para alteração da data de um agendamento."""
    return alterar_data_agendamento(id)