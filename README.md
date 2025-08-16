# 📝 API de Cadastro de Usuários

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-brightgreen.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-yellow.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)

API simples desenvolvida com **FastAPI** e **MySQL** para realizar operações de CRUD (Create, Read, Update, Delete) em uma tabela de usuários.  

---

## 🚀 Tecnologias Utilizadas
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) – Framework web moderno
- 🔥 [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI rápido
- 🗄️ [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/) – Driver de conexão com MySQL
- 🐬 Banco de Dados **MySQL**

---

## 📂 Estrutura do Projeto
📦 meu_projeto
- main.py → Arquivo principal da API
- crud.py → Funções de CRUD no banco
- database.py → Conexão com o MySQL
- requirements.txt → Dependências do projeto
- README.md → Documentação

 

## ⚙️ Configuração do Banco de Dados

Crie um banco de dados MySQL e configure a tabela `users`:

```sql
CREATE DATABASE IF NOT EXISTS seu_banco;

USE seu_banco;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL
);
Edite o arquivo database.py com suas credenciais:

📦 Instalação
Clone o repositório:

git clone https://github.com/seuusuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
Instale as dependências:

pip install -r requirements.txt
▶️ Executando a API
Inicie o servidor com Uvicorn:

uvicorn main:app --reload

Documentação automática:

📘 Swagger UI

📕 ReDoc


📌 Dependências
No arquivo requirements.txt:
fastapi
uvicorn
mysql-connector-python

✨ Autor
Bruno Correia



