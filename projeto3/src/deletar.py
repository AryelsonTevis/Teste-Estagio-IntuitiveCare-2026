from sqlalchemy import create_engine, text

def deletar_tabela():
    usuario = "avnadmin"
    senha = "AVNS_ijq0-CSazBOLOdhlqbI"
    host = "estagiobd-testebd.f.aivencloud.com"
    porta = "27428"
    banco = "defaultdb"

    url_conexao = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}?ssl_disabled=false"
    
    try:
        engine = create_engine(url_conexao, connect_args={"ssl": {"fake_config": True}})
        
        with engine.connect() as conexao:
            # O comando text() é necessário no SQLAlchemy 2.0+
            conexao.execute(text("DROP TABLE IF EXISTS dados_trimestre;"))
            # No MySQL, DROP TABLE é auto-commit, mas usar a transação é boa prática
            conexao.commit()
            
        print("Tabela 'despesas' excluída com sucesso!")
        
    except Exception as e:
        print(f"Erro ao excluir tabela: {e}")

# Executar a função
deletar_tabela()