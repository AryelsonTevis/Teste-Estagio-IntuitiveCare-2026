import extrair , detectar , criar_csv ,endpoints ,compactar_para_zip

#baixar os arquivos dos 3 últimos trimestres e a lista de ANS ativos
endpoints.get_last_quarters(["1T2025.zip", "2T2025.zip", "3T2025.zip"])
endpoints.get_active_ans()

#extrair, detectar, criar csv e compactar
extrair.extract_zip(1,2,3)
linhas = detectar.filtered_lines(1,2,3)
arquivo_filtrado = detectar.filtered_file(linhas, 'data/csv/planos_de_saude_ativos.csv')
arquivo_formatado = detectar.format_values(arquivo_filtrado)
criar_csv.create_csv_file(arquivo_formatado)
compactar_para_zip.compact_result()