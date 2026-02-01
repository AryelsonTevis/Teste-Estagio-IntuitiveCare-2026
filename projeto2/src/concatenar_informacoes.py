import pandas as pd

def criar_arquivo_final(df_final, planos_de_saude_ativos):
    
    try:
        
        df_cadop = pd.read_csv(planos_de_saude_ativos, sep=';', encoding='latin1')

        
        df_final['CNPJ'] = pd.to_numeric(df_final['CNPJ'])
        df_cadop['CNPJ'] = pd.to_numeric(df_cadop['CNPJ'])
        df_cadop['RegistroANS'] = pd.to_numeric(df_cadop['REGISTRO_OPERADORA'], errors='coerce')

        

        
        df_concatenado = pd.merge(
            df_final, 
            df_cadop[['Modalidade', 'CNPJ', 'UF', 'RegistroANS']], 
            left_on='CNPJ', 
            right_on='CNPJ', 
            how='inner'
        )

        df_consolidado = df_concatenado.groupby(['Razao_Social','UF', 'Trimestre']).agg({
            'ValorDespesas': 'mean',
            'RegistroANS': 'first',
            'CNPJ': 'first',
            'Modalidade': 'first',
            'Ano': 'first'           
        }).reset_index()
        df_consolidado = df_consolidado.rename(columns={'ValorDespesas': 'MediaDespesas'})
        
        
        return df_consolidado
    
    except Exception as e:
        print(f"Erro no cruzamento: {e}")
        return None

def formatar_valores(df):
    try:
        colunas_finais = ['RegistroANS','CNPJ', 'Razao_Social','Modalidade','UF', 'Trimestre', 'Ano', 'MediaDespesas']
        df = df[colunas_finais]
        df = df.sort_values(by='MediaDespesas', ascending=False)
        df['MediaDespesas'] = df['MediaDespesas'].apply(lambda x: f" {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        
        return df
    except Exception as e:
        print(f"Erro na formatação dos valores: {e}")
        return df
    
    