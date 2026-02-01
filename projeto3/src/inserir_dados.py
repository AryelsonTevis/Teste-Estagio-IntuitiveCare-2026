import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env



# ... e assim por diante

def inserir_no_banco(despesas, planos_saude, trimestres):
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    banco = os.getenv("DB_NAME")

    # construindo a string de conexão
    url_conexao = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"
    
    try:
       
        engine = create_engine(url_conexao)
#---------------------------------------arquivo despesas agregadas------------------------------------------------------
        df_despesas = pd.read_csv(despesas, sep=';', encoding='utf-8-sig')

        if 'MediaDespesas' in df_despesas.columns:
            df_despesas['MediaDespesas'] = df_despesas['MediaDespesas'].astype(str)
            df_despesas['MediaDespesas'] = (
                df_despesas['MediaDespesas']
                .str.replace(r'[^\d,.-]', '', regex=True) # Remove tudo que não for número, vírgula ou ponto
                .str.replace('.', '', regex=False)       # Remove ponto de milhar
                .str.replace(',', '.', regex=False)       # Troca vírgula decimal por ponto
                .str.strip()
            )
            df_despesas['MediaDespesas'] = pd.to_numeric(df_despesas['MediaDespesas'], errors='coerce').fillna(0.0)
        
    
        cols_texto = ['Razao_Social', 'Modalidade']
        for col in cols_texto:
            if col in df_despesas.columns:
                df_despesas[col] = df_despesas[col].apply(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)     

        df_despesas.to_sql(name='despesas', con=engine, if_exists='append', index=False, chunksize=500)

#------------------------------------------------------------------------------------------------------------------------
#---------------------------------------arquivo planos de saude----------------------------------------------------------
        df_planos = pd.read_csv(planos_saude, sep=';', encoding='latin1')

        df_planos['Nome_Fantasia'] = df_planos['Nome_Fantasia'].fillna(df_planos['Razao_Social'])

        df_planos['DDD'] = df_planos['DDD'].astype(str).str.replace(r'\.0$', '', regex=True)
        df_planos['DDD'] = df_planos['DDD'].str.extract(r'(\d+)').fillna('')

        df_planos = df_planos.fillna("Não Informado")

        
        df_planos.to_sql(name='planos_saude', con=engine, if_exists='append', index=False, chunksize=500)
#------------------------------------------------------------------------------------------------------------------------
#---------------------------------------arquivo dados trimestres---------------------------------------------------------
        df_tri = pd.read_csv(trimestres, sep=';', encoding='latin1')


        if 'ValorDespesas' in df_tri.columns:
            df_tri['ValorDespesas'] = df_tri['ValorDespesas'].astype(str)
            df_tri['ValorDespesas'] = (
                df_tri['ValorDespesas']
                .str.replace(r'[^\d,.-]', '', regex=True) # Remove tudo que não for número, vírgula ou ponto
                .str.replace('.', '', regex=False)       # Remove ponto de milhar
                .str.replace(',', '.', regex=False)       # Troca vírgula decimal por ponto
                .str.strip()
            )
            df_tri['ValorDespesas'] = pd.to_numeric(df_tri['ValorDespesas'], errors='coerce').fillna(0.0)

        df_tri.to_sql(name='dados_trimestre', con=engine, if_exists='append', index=False, chunksize=500)

        
        print("Dados inseridos com sucesso!")
        return True

    except Exception as e:
        print(f"Erro ao inserir no banco: {e}")