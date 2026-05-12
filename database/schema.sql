CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    telefone VARCHAR(20) NOT NULL,

    email VARCHAR(100) UNIQUE
);

--------------------------------------------------

CREATE TABLE servicos (
    id SERIAL PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    preco NUMERIC(10,2) NOT NULL,

    duracao INTEGER NOT NULL
);

--------------------------------------------------

CREATE TABLE agendamentos (
    id SERIAL PRIMARY KEY,

    data_hora TIMESTAMP NOT NULL,

    status VARCHAR(30) DEFAULT 'PENDENTE',

    cliente_id INTEGER NOT NULL,

    servico_id INTEGER NOT NULL,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id),

    CONSTRAINT fk_servico
        FOREIGN KEY (servico_id)
        REFERENCES servicos(id)
);