import extrair , detectar , criar_csv ,endpoints ,compactar_para_zip

#baixar os arquivos dos 3 últimos trimestres e a lista de ANS ativos
endpoints.get_last_quarters(["1T2025.zip", "2T2025.zip", "3T2025.zip"])
endpoints.get_active_ans()

#extrair, detectar, criar csv e compactar
extrair.extrair_zip(1,2,3)
linhas = detectar.linhas_filtradas(1,2,3)
arquivo_filtrado = detectar.criar_arquivo_final(linhas, 'data/csv/planos_de_saude_ativos.csv')
arquivo_formatado = detectar.formatar_valores(arquivo_filtrado)
criar_csv.criar_arquivo_csv(arquivo_formatado)
compactar_para_zip.compactar_resultado()