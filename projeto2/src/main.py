import validacoes, criar_csv, endpoints, concatenar_informacoes, compactar_para_zip

# Validar e processar os arquivos dos 3 últimos trimestres
processado = validacoes.validate_and_process_file()

# Baixar a lista de ANS ativos
endpoints.get_active_ans()

# Concatenar, formatar e criar o CSV final
arquivo_filtrado = concatenar_informacoes.create_final_file(processado, 'data/csv/planos_de_saude_ativos.csv')
arquivo_final_formatado = concatenar_informacoes.format_values(arquivo_filtrado)
criar_csv.create_csv_file(arquivo_final_formatado)
compactar_para_zip.compact_result()