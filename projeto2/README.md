# 📊 Projeto 2 – Processamento e Normalização de Dados

## 📌 Descrição
Este projeto em Python tem como objetivo **processar, validar, normalizar e consolidar dados** provenientes de arquivos compactados (ZIP), gerando arquivos CSV prontos para análise.

Ele foi pensado para lidar com **estruturas diferentes de arquivos**, garantindo padronização, validação dos dados e organização do resultado final.

---

## 📁 Estrutura do Projeto
```
│
├── data/
│ ├── csv/
│ │ └── dados_trimestres_concatenados.csv
│ ├── processados/
│ └── zip/
│
├── src/
│ ├── main.py
│ ├── endpoints.py
│ ├── validacoes.py
│ ├── criar_csv.py
│ ├── concatenar_informacoes.py
│ └── compactar_para_zip.py
│
└── README.md
```
---

## ⚙️ Funcionalidades
- 📂 Leitura de arquivos ZIP
- 📄 Processamento de arquivos CSV
- 🔍 Validação e tratamento de dados
- 🔄 Concatenação de informações de múltiplos arquivos
- 📊 Geração de CSV consolidado
- 🗜️ Compactação dos arquivos processados em ZIP

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas**
- **Requests** 



---
## 📦 Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- `openpyxl`
- `pandas`
---

## ▶️ Como Executar o Projeto
1️⃣ Acesse a pasta do projeto
cd projeto2

2️⃣ Instale as dependências
pip install pandas openpyxl

3️⃣ Execute o projeto
python src/main.py ou py src/main.py
