import validacoes, criar_csv, endpoints, concatenar_informacoes, compactar_para_zip

processado = validacoes.validar_e_processar_arquivo()
endpoints.get_active_ans()
arquivo_filtrado = concatenar_informacoes.criar_arquivo_final(processado, 'data/csv/planos_de_saude_ativos.csv')
arquivo_final_formatado = concatenar_informacoes.formatar_valores(arquivo_filtrado)
criar_csv.criar_arquivo_csv(arquivo_final_formatado)
compactar_para_zip.compactar_resultado()