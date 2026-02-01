import pymysql

def criar_tabelas():
    config={
        'host': 'estagiobd-testebd.f.aivencloud.com',
        'port': 27428,
        'user': 'avnadmin',
        'password':'AVNS_ijq0-CSazBOLOdhlqbI',
        'database':'defaultdb'
    }
    conexao = None

    try:
        conexao = pymysql.connect(**config)
        cursor = conexao.cursor()

        criar_tabela_daspesas_agregadas = """
        CREATE TABLE IF NOT EXISTS despesas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            RegistroANS INT NOT NULL,
            CNPJ VARCHAR(20) NOT NULL,
            Razao_Social VARCHAR(255) NOT NULL,
            Modalidade VARCHAR(100) NOT NULL,
            UF VARCHAR(2) NOT NULL,
            Trimestre INT NOT NULL,
            Ano INT NOT NULL,
            MediaDespesas DECIMAL(15, 2) NOT NULL
        );
        """
        criar_tabela_planos_saude = """
        CREATE TABLE IF NOT EXISTS planos_saude (
            id INT AUTO_INCREMENT PRIMARY KEY,
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
        );
        """
        
        criar_tabela_dados_trimestes = """
        CREATE TABLE IF NOT EXISTS dados_trimestre (
            id INT AUTO_INCREMENT PRIMARY KEY,
            CNPJ VARCHAR(20) NOT NULL,
            Razao_Social VARCHAR(255) NOT NULL,
            Trimestre INT NOT NULL,
            Ano INT NOT NULL,
            ValorDespesas DECIMAL(15, 2) NOT NULL
        );
        """
        cursor.execute(criar_tabela_daspesas_agregadas)
        cursor.execute(criar_tabela_planos_saude)
        cursor.execute(criar_tabela_dados_trimestes)

        
        conexao.commit()
        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if conexao is not None:
            conexao.close()
            print("Conexão encerrada.")