import pandas as pd 

def create_csv_file(linhas):
    linhas.to_csv('data/processados/despesas_agregadas.csv',sep=';', index=False, encoding='utf-8')
