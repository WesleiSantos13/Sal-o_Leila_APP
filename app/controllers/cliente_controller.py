from flask import request, jsonify
from app.extensions import db
from app.models.cliente_model import Cliente
from app.models.agendamento_model import Agendamento


def criar_cliente():
    """Verifica se o cliente já existe pelo e-mail; caso contrário, cria um novo registro."""
    dados = request.json
    cliente_existente = Cliente.query.filter_by(email=dados["email"]).first()

    if cliente_existente:
        return jsonify({
            "id": cliente_existente.id,
            "nome": cliente_existente.nome
        }), 200

    novo_cliente = Cliente(
        nome=dados["nome"],
        telefone=dados["telefone"],
        email=dados["email"]
    )

    db.session.add(novo_cliente)
    db.session.commit()

    return jsonify({
        "id": novo_cliente.id,
        "nome": novo_cliente.nome
    }), 201


def listar_clientes():
    """Retorna uma lista em formato JSON com todos os clientes cadastrados no banco de dados."""
    clientes = Cliente.query.all()
    resultado = []

    for cliente in clientes:
        resultado.append({
            'id': cliente.id,
            'nome': cliente.nome,
            'telefone': cliente.telefone,
            'email': cliente.email
        })

    return jsonify(resultado)


def deletar_cliente(id):
    """Remove um cliente se ele existir e não possuir agendamentos vinculados (integridade de dados)."""
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    agendamentos_vinculados = Agendamento.query.filter_by(cliente_id=id).first()
    
    if agendamentos_vinculados:
        return jsonify({
            "erro": "Este cliente não pode ser apagado pois possui agendamentos/serviços no sistema."
        }), 400 

    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"mensagem": "Cliente removido"}), 200