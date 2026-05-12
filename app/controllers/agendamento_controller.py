from flask import request, jsonify
from datetime import datetime
from app.models.cliente_model import Cliente 
from app.extensions import db
from app.models.agendamento_model import Agendamento

def criar_agendamento():
    """Processa a criação de novos agendamentos para múltiplos serviços de um cliente na mesma data e hora."""
    dados = request.json

    # Converte a string que vem do HTML (ex: "2026-05-15T14:30") para objeto datetime do Python
    data_hora = datetime.strptime(
        dados['data_hora'],
        "%Y-%m-%dT%H:%M"
    )

    cliente_id = dados.get("cliente_id")
    
    # Agora pegamos a lista de serviços (array) enviada pelo novo frontend
    servicos_ids = dados.get("servicos_ids", [])

    # Validação: Se a lista estiver vazia, retorna um erro
    if not servicos_ids:
        return jsonify({'erro': 'Nenhum serviço selecionado'}), 400

    # Para cada ID de serviço na lista, cria um agendamento no banco
    for s_id in servicos_ids:
        agendamento = Agendamento(
            data_hora=data_hora,
            cliente_id=cliente_id,
            servico_id=s_id,
            status=dados.get("status", "Agendado") # Inclui o status inicial
        )
        db.session.add(agendamento)

    # Salva todos os serviços selecionados de uma só vez
    db.session.commit()

    return jsonify({
        'mensagem': f'{len(servicos_ids)} agendamento(s) criado(s) com sucesso'
    }), 201


def listar_agendamentos():
    """Retorna uma lista completa de todos os agendamentos registrados no sistema."""
    agendamentos = Agendamento.query.all()

    resultado = []

    for agendamento in agendamentos:
        resultado.append({
            'id': agendamento.id,
            'data_hora': agendamento.data_hora,
            'status': agendamento.status,
            'cliente_id': agendamento.cliente_id,
            'servico_id': agendamento.servico_id
        })

    return jsonify(resultado)


def atualizar_status(id):
    """Localiza um agendamento pelo ID e atualiza o seu status (ex: Confirmado, Realizado)."""
    agendamento = Agendamento.query.get(id)
    
    if not agendamento:
        return jsonify({
            "erro": "Agendamento não encontrado"
        }), 404
        
    dados = request.json
    
    # Atualiza apenas o status se ele for enviado na requisição
    if "status" in dados:
        agendamento.status = dados["status"]
        
    db.session.commit()
    
    return jsonify({
        "mensagem": "Status atualizado com sucesso!"
    }), 200


def deletar_agendamento(id):
    """Remove definitivamente um registro de agendamento do banco de dados através do ID."""
    agendamento = Agendamento.query.get(id)

    if not agendamento:
        return jsonify({
            "erro": "Agendamento não encontrado"
        }), 404

    db.session.delete(agendamento)
    db.session.commit()

    return jsonify({
        "mensagem": "Agendamento removido"
    })


def buscar_historico_cliente():
    """Filtra e retorna todos os agendamentos vinculados ao e-mail de um cliente específico."""
    email = request.args.get("email")
    cliente = Cliente.query.filter_by(email=email).first()
    
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado"}), 404
        
    # Busca os agendamentos desse cliente específico
    agendamentos = Agendamento.query.filter_by(cliente_id=cliente.id).all()
    
    resultado = []
    for a in agendamentos:
        resultado.append({
            "id": a.id,
            "data_hora": a.data_hora.strftime("%Y-%m-%dT%H:%M"),
            "servico_id": a.servico_id,
            "status": a.status
        })
        
    return jsonify(resultado), 200


def alterar_data_agendamento(id):
    """Modifica a data e o horário de um agendamento existente, convertendo o formato recebido."""
    dados = request.json
    agendamento = Agendamento.query.get(id)
    
    if not agendamento:
        return jsonify({"erro": "Agendamento não encontrado"}), 404
        
    # Converte a nova data enviada
    nova_data = datetime.strptime(dados['data_hora'], "%Y-%m-%dT%H:%M")
    
    # Atualiza a data
    agendamento.data_hora = nova_data
    db.session.commit()
    
    return jsonify({"mensagem": "Data alterada com sucesso"}), 200