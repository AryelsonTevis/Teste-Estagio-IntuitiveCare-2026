import pandas as pd 

def create_csv_file(linhas_filtradas):
    linhas_filtradas.to_csv('data/processados/dados_trimestres_concatenados.csv',sep=';', index=False, encoding='utf-8')
