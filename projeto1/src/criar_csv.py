import pandas as pd 

def criar_arquivo_csv(linhas_filtradas):
    linhas_filtradas.to_csv('data/processados/dados_trimestres_concatenados.csv',sep=';', index=False, encoding='utf-8')
