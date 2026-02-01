import pandas as pd

def linhas_filtradas(t1, t2, t3):
    trimestres = [t1, t2, t3]
    lista_linhas = []
    for t in trimestres:
        caminho = f'data/csv/{t}T2025.csv'
        try:
            df = pd.read_csv(caminho, sep=';')
            # Aplicar filtro na coluna 'DESCRICAO'
            filtro = df['DESCRICAO'].str.contains('Despesas com Eventos/Sinistros', case=False, na=False)
            df_filtrado = df[filtro].copy()
            # Adicionar coluna TRIMESTRE_ORIGEM
            df_filtrado['TRIMESTRE_ORIGEM'] = f'{t}T'
            
            lista_linhas.append(df_filtrado)
            
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {caminho}")
    # Concatenar todas as linhas filtradas em um único DataFrame
    if lista_linhas:
        df_final = pd.concat(lista_linhas, ignore_index=True)
        
        return df_final
    else:
        return "Nenhum dado encontrado."
    
def criar_arquivo_final(df_final, planos_de_saude_ativos):
    
    try:
        
        df_cadop = pd.read_csv(planos_de_saude_ativos, sep=';', encoding='latin1')

        # Garantir que as colunas de junção sejam do mesmo tipo
        df_final['REG_ANS'] = pd.to_numeric(df_final['REG_ANS'])
        df_cadop['REGISTRO_OPERADORA'] = pd.to_numeric(df_cadop['REGISTRO_OPERADORA'])

        # Remover valores Null antes do merge
        df_final = df_final.dropna(subset=['REG_ANS'])
        df_cadop = df_cadop.dropna(subset=['REGISTRO_OPERADORA'])

        # Realizar a junção entre os DataFrames
        df_final = pd.merge(
            df_final, 
            df_cadop[['REGISTRO_OPERADORA', 'CNPJ', 'Razao_Social']], 
            left_on='REG_ANS', 
            right_on='REGISTRO_OPERADORA', 
            how='inner'
        )

        return df_final

    except Exception as e:
        print(f"Erro no cruzamento: {e}")
        return None

def formatar_valores(df):
    try:
        # Converter a coluna DATA para datetime
        df['DATA'] = pd.to_datetime(df['DATA'])

        # Extrair Ano e Trimestre
        df['Ano'] = df['DATA'].dt.year
        df['Trimestre'] = df['DATA'].dt.quarter

        # Converter valores para float
        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].astype(str).str.replace(',', '.').astype(float)
        df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].astype(str).str.replace(',', '.').astype(float)

        # Calcular ValorDespesas
        df['ValorDespesas'] = df['VL_SALDO_INICIAL'] - df['VL_SALDO_FINAL']
        df['ValorDespesas'] = df['ValorDespesas'].apply(lambda x: f" {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        # Selecionar colunas finais
        colunas_finais = ['CNPJ', 'Razao_Social', 'Trimestre', 'Ano', 'ValorDespesas']
        return df[colunas_finais]
    except Exception as e:
        print(f"Erro na formatação dos valores: {e}")
        return df

