import zipfile

def extrair_zip(t1, t2, t3):
    trimestres = [t1, t2, t3]
    pasta_destino = 'data/csv/'
    for t in trimestres:
        caminho_zip = f'data/zip/{t}T2025.zip'
        
        try:
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
                print(f"Sucesso: {t}T2025.zip extraído para {pasta_destino}")
        except FileNotFoundError:
            print(f"Erro: O arquivo {caminho_zip} não foi encontrado.")
        except zipfile.BadZipFile:
            print(f"Erro: O arquivo {caminho_zip} está corrompido ou não é um ZIP.")