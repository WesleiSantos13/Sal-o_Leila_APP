from app.extensions import db
from datetime import datetime


class Agendamento(db.Model):
    __tablename__ = "agendamentos"

    id = db.Column(db.Integer, primary_key=True)

    data_hora = db.Column(db.DateTime, nullable=False)

    status = db.Column(
        db.String(30),
        default='PENDENTE'
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.id'),
        nullable=False
    )

    servico_id = db.Column(
        db.Integer,
        db.ForeignKey('servicos.id'),
        nullable=False
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )