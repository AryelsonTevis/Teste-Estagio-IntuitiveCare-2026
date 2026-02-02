import re
import pandas as pd
import numpy as np

def validate_and_process_file():
    arquivo_base = "data/csv/dados_trimestres_concatenados.csv"
    try:
        df = pd.read_csv(arquivo_base, sep=';')
        print("Arquivo carregado com sucesso.")

        #validar CNPJ    
        df['CNPJ_VALIDADO'] = df['CNPJ'].apply(validate_cnpj)
        
        df['CNPJ_VALIDADO'] = df['CNPJ_VALIDADO'].map({True: 'Valido', False: 'Invalido'})
        
        
        #validar numeros na coluna 'VALOR'
        condicoes = [
        (df['ValorDespesas'] > 0),
        (df['ValorDespesas'] == 0),
        (df['ValorDespesas'] < 0)
        ]
        resultado = ["saldo positivo.", "saldo zerado.", "saldo negativo."]
        df['VALOR'] = np.select(condicoes, resultado, default="valor inválido.")


        return df
    except FileNotFoundError:
        print(f"Arquivo não encontrado!")
        return None

def validate_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', str(cnpj))
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False
    
    def calculate_digit(cnpj, peso):
        soma = sum(int(num) * peso for num, peso in zip(cnpj, peso))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [6,  5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    digito1 = calculate_digit(cnpj[:12], peso1)
    if cnpj[12] != digito1:
        
        return False
    
    digito2 = calculate_digit(cnpj[:13], peso2)
    if cnpj[13] != digito2:
        
        return False
    
    
    return True


