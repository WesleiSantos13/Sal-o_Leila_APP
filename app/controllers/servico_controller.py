from flask import request, jsonify
from app.extensions import db
from app.models.servico_model import Servico
from app.models.agendamento_model import Agendamento

def criar_servico():
    """Recebe os dados da requisição JSON e cria um novo serviço no banco de dados."""
    dados = request.json

    servico = Servico(
        nome=dados['nome'],
        preco=dados['preco'],
        duracao=dados['duracao']
    )

    db.session.add(servico)
    db.session.commit()

    return jsonify({
        'mensagem': 'Serviço criado com sucesso'
    }), 201


def listar_servicos():
    """Busca e retorna uma lista com todos os serviços cadastrados no sistema."""
    servicos = Servico.query.all()

    resultado = []

    for servico in servicos:
        resultado.append({
            'id': servico.id,
            'nome': servico.nome,
            'preco': servico.preco,
            'duracao': servico.duracao
        })

    return jsonify(resultado)


def deletar_servico(id):
    """Busca um serviço pelo ID e o remove do banco de dados."""
    servico = Servico.query.get(id)

    if not servico:
        return jsonify({
            "erro": "Serviço não encontrado"
        }), 404
    
    agendamentos_vinculados = Agendamento.query.filter_by(servico_id=id).first()
    # Se o serviço estiver vinculado a um agendamento
    if agendamentos_vinculados:
        return jsonify({
            "erro": "Este serviço não pode ser apagado pois possui agendamentos no sistema!"
        }), 400 

    db.session.delete(servico)
    db.session.commit()

    return jsonify({
        "mensagem": "Serviço removido com sucesso!"
    })


def atualizar_servico(id):
    """Busca um serviço pelo ID e atualiza suas informações (nome, preço e duração)."""
    servico = Servico.query.get(id)

    if not servico:
        return jsonify({
            "erro": "Serviço não encontrado"
        }), 404
    
    agendamentos_vinculados = Agendamento.query.filter_by(servico_id=id).first()
    # Se o serviço estiver vinculado a um agendamento
    if agendamentos_vinculados:
        return jsonify({
            "erro": "Este serviço não pode ser editado pois possui agendamentos no sistema."
        }), 400 
    else:
        dados = request.json
        servico.nome = dados["nome"]
        servico.preco = dados["preco"]
        servico.duracao = dados["duracao"]
        db.session.commit()

        return jsonify({
            "mensagem": "Serviço atualizado"
        })
        
