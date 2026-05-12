# 💇‍♀️ Salão da Leila — Sistema de Agendamento

Sistema web desenvolvido para automatizar o agendamento de serviços do **Salão da Leila**, proporcionando uma melhor experiência para os clientes e oferecendo ferramentas de gestão operacional e gerencial para a proprietária.

---

# 📋 Sobre o Projeto

Este projeto foi desenvolvido como uma solução personalizada para o gerenciamento de agendamentos de um salão de beleza, permitindo:

- Agendamento online de serviços;
- Gestão de clientes;
- Controle operacional dos atendimentos;
- Dashboard gerencial com métricas do salão;
- Organização dos serviços realizados;
- Melhor experiência para clientes e administradores.

---

# 🚀 Tecnologias Utilizadas

## Backend
- Python 3
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

## Banco de Dados
- SQLite (desenvolvimento)
- PostgreSQL (Não fiz a migração)

## Frontend
- HTML5
- CSS3
- JavaScript

## Arquitetura e Organização
- MVC (Model-View-Controller)
- Blueprints do Flask
- Controllers para regras de negócio

---

# 📂 Estrutura do Projeto

```bash
Sal-o_Leila_APP/
│
├── app/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   └── services/
│
├── instance/
├── migrations/
├── venv/
├── requirements.txt
├── run.py
└── README.md
```

---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone <https://github.com/WesleiSantos13/Sal-o_Leila_APP>
```

ou extraia os arquivos do projeto.

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd Sal-o_Leila_APP
```

---

## 3️⃣ Crie e ative o ambiente virtual

### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Execute a aplicação

```bash
python run.py
```

---

## 6️⃣ Acesse no navegador

```bash
http://127.0.0.1:5000
```

---

# ✅ Funcionalidades

## 👤 Área do Cliente

- Cadastro de clientes;
- Agendamento de um ou múltiplos serviços;
- Histórico completo de agendamentos;
- Alteração de agendamentos;
- Sugestão inteligente de agrupamento de serviços;
- Bloqueio de alteração com menos de 48 horas.

---

## 🛠️ Painel Administrativo

### Operacional
- Confirmação de agendamentos;
- Alteração de datas sem restrição;
- Gerenciamento individual dos serviços;
- Controle de status dos atendimentos.

### Gerencial
- Dashboard semanal;
- Volume de serviços concluídos;
- Estimativa de faturamento.

---

# 📌 Regras de Negócio

## ✔️ Agendamento Múltiplo
O cliente pode selecionar vários serviços em um único agendamento.

## ✔️ Alteração com Antecedência
Alterações online são permitidas apenas com no mínimo 48 horas de antecedência.

## ✔️ Contato Direto com o Salão
Caso o serviço esteja próximo da data, o sistema orienta o cliente a entrar em contato diretamente com o salão.

## ✔️ Sugestão Inteligente
Ao detectar agendamentos na mesma semana, o sistema sugere agrupar os serviços para maior comodidade.

## ✔️ Integridade de Dados
Clientes com serviços vinculados não podem ser excluídos, garantindo consistência histórica e financeira.

---

# 🧠 Boas Práticas Aplicadas

- Separação de responsabilidades com Controllers;
- Organização modular utilizando Blueprints;
- Uso de Docstrings para documentação;
- Estrutura preparada para testes unitários futuros;
- Regras de negócio centralizadas no backend.

---

# 📊 Objetivo do Projeto

Este sistema foi desenvolvido como parte de um **teste técnico para vaga de estágio**, com foco em:

- Organização de projeto;
- Boas práticas de programação;
- Arquitetura de software;
- Modelagem de regras de negócio;
- Desenvolvimento Full Stack com Flask.

---

# 👨‍💻 Autor

Desenvolvido por **Weslei Santos**.