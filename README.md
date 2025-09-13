# 📚 Curso de FastAPI – REST API com Python (Backend Completo)

Este repositório contém os estudos e implementações realizados durante o curso **[Curso de FastAPI – Rest API com Python (Backend Completo)](https://youtu.be/BtIy2aD8k_w?si=Zqlz8edT8cS7TkpW)**, ministrado pela Hashtag Programação.

---

## 🎯 Objetivo

Aprender a desenvolver uma API REST completa utilizando o framework **FastAPI**, explorando desde conceitos básicos até autenticação, banco de dados, segurança e boas práticas de desenvolvimento backend.

---

## 📂 Conteúdo do Curso

| Aula | Tema principal |
|------|----------------|
| **1** | Introdução ao projeto de pizzaria delivery, configuração inicial, execução local, documentação automática da API |
| **2** | Criação de rotas HTTP (GET, POST, PUT, DELETE), funções assíncronas e autenticação básica |
| **3** | Banco de dados com SQLAlchemy, modelos de dados e migrações com Alembic |
| **4** | Cadastro de usuário, schemas Pydantic e criptografia de senhas |
| **5** | Autenticação de usuários com JWT (JSON Web Tokens) |
| **6** | Configuração de variáveis de ambiente e autenticação avançada |
| **7** | Controle de acesso para usuários e funções específicas |
| **9** | Gerenciamento de pedidos: visualizar, remover itens, calcular preços |
| **10** | Finalização de pedidos, padronização de respostas e schemas de saída |

---

## 🛠️ Tecnologias Utilizadas

- **Python**  
- **FastAPI** (framework principal)  
- **Uvicorn** (servidor ASGI)  
- **Pydantic** (validação e schemas)  
- **SQLAlchemy** (ORM)  
- **Alembic** (migrações de banco de dados)  
- **JWT** (autenticação segura)  

---

## ⚙️ Pré-requisitos

- Python 3.10+ instalado  
- Git instalado  
- Conhecimentos básicos de Python e HTTP  
- Noções de SQL ajudam no entendimento  

---

## 🚀 Como rodar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/StortiI25/FastAPI-Python.git
   cd fastapi-curso
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Rode o servidor:

bash
Copiar código
uvicorn main:app --reload
Acesse a documentação interativa:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📌 O que aprendi
Criar rotas e organizar endpoints

Trabalhar com banco de dados relacional via SQLAlchemy

Realizar migrações com Alembic

Implementar autenticação com JWT

Proteger rotas e aplicar controle de acesso

Documentar a API automaticamente

🧑‍💻 Autor
Curso disponibilizado pela Hashtag Programação.
Este repositório é apenas para fins de estudo e prática.
