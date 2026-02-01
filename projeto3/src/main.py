import endpoints, criar_tabelas, inserir_dados

# Baixar a lista de ANS ativos
endpoints.get_active_ans()

# Criar as tabelas no banco de dados
criar_tabelas.criar_tabelas()

# Inserir os dados nos bancos de dados
inserir_dados.inserir_no_banco("data/csv/despesas_agregadas.csv","data/csv/planos_de_saude_ativos.csv","data/csv/dados_trimestres_concatenados.csv")

