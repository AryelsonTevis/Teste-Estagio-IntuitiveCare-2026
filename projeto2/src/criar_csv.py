import pandas as pd 

def criar_arquivo_csv(linhas):
    linhas.to_csv('data/processados/despesas_agregadas.csv',sep=';', index=False, encoding='utf-8')
