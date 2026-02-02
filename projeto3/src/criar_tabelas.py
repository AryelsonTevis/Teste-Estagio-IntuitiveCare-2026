from dotenv import load_dotenv
from sqlalchemy import create_engine,text
import os

def create_tables():
    load_dotenv()
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    banco = os.getenv("DB_NAME")

    # construindo a string de conexão
    url_conexao = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"
    

    engine = create_engine(url_conexao)

    #criando as tabelas
    queries = [""" CREATE TABLE IF NOT EXISTS despesas (id INT AUTO_INCREMENT PRIMARY KEY,
        RegistroANS INT NOT NULL,
        CNPJ VARCHAR(20) NOT NULL,
        Razao_Social VARCHAR(255) NOT NULL,
        Modalidade VARCHAR(100) NOT NULL,
        UF VARCHAR(2) NOT NULL,
        Trimestre INT NOT NULL,
        Ano INT NOT NULL,
        MediaDespesas DECIMAL(15, 2) NOT NULL
    );""",

    """CREATE TABLE IF NOT EXISTS planos_saude (id INT AUTO_INCREMENT PRIMARY KEY,
        REGISTRO_OPERADORA INT NOT NULL,
        CNPJ VARCHAR(20) NOT NULL,
        Razao_Social VARCHAR(255) NOT NULL,
        Nome_Fantasia VARCHAR(255) NOT NULL,
        Modalidade VARCHAR(100) NOT NULL,
        Logradouro VARCHAR(255) NOT NULL,
        Numero VARCHAR(20) NOT NULL,
        Complemento VARCHAR(255),
        Bairro VARCHAR(100) NOT NULL,
        Cidade VARCHAR(100) NOT NULL,
        UF VARCHAR(2) NOT NULL,
        CEP VARCHAR(10) NOT NULL,
        DDD VARCHAR(5) NOT NULL,
        Telefone VARCHAR(20) NOT NULL,
        Fax VARCHAR(20),
        Endereco_Eletronico VARCHAR(255) NOT NULL,
        Representante VARCHAR(255) NOT NULL,
        Cargo_Representante VARCHAR(100) NOT NULL,
        Regiao_de_Comercializacao VARCHAR(100) NOT NULL,
        Data_Registro_ANS DATE NOT NULL
    );""",

    """CREATE TABLE IF NOT EXISTS dados_trimestre (id INT AUTO_INCREMENT PRIMARY KEY,
        CNPJ VARCHAR(20) NOT NULL,
        Razao_Social VARCHAR(255) NOT NULL,
        Trimestre INT NOT NULL,
        Ano INT NOT NULL,
        ValorDespesas DECIMAL(15, 2) NOT NULL
    );"""
        ]
    # executando as queries
    with engine.begin() as conn:
        for query in queries:
            conn.execute(text(query))
        print("Tabelas criadas com sucesso.")
    