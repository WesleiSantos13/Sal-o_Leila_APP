INSERT INTO servicos (
    nome,
    preco,
    duracao
)
VALUES
('Corte Feminino', 50.00, 40),
('Escova', 80.00, 60),
('Hidratação', 120.00, 90),
('Progressiva', 250.00, 180),
('Manicure', 35.00, 30),
('Pedicure', 40.00, 40);

--------------------------------------------------

INSERT INTO clientes (
    nome,
    telefone,
    email
)
VALUES
(
    'Maria Silva',
    '75999999999',
    'maria@email.com'
),
(
    'Ana Souza',
    '75888888888',
    'ana@email.com'
);

--------------------------------------------------

INSERT INTO agendamentos (
    data_hora,
    status,
    cliente_id,
    servico_id
)
VALUES
(
    '2026-05-15 14:00:00',
    'CONFIRMADO',
    1,
    1
),
(
    '2026-05-16 10:30:00',
    'PENDENTE',
    2,
    3
);