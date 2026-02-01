import requests

base_url = "https://dadosabertos.ans.gov.br/FTP/PDA"
def get_active_ans():
    try:
        response = requests.get(base_url + "/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv")
        if response.status_code == 200:
        
            with open("data/csv/" + "planos_de_saude_ativos.csv", "wb") as arquivo:
                arquivo.write(response.content)
            print("Arquivo salvo com sucesso na mesma pasta do seu script!")
        else:
            print(f"Erro ao baixar: {response.status_code}")
            
    except Exception as e:
        print(f"Ocorreu um erro na conexão: {e}")
        return None

