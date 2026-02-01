import zipfile
import os

def compactar_resultado():
    caminho_zip = os.path.join("data/zip", "consolidado_despesas.zip")
    try:
        
        with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            zipf.write("data/processados/dados_trimestres_concatenados.csv", os.path.basename("data/processados/dados_trimestres_concatenados.csv"))
        
        print(f"Sucesso! Arquivo {"consolidado_despesas.zip"} criado com sucesso.")
    except Exception as e:
        print(f"Erro ao compactar: {e}")