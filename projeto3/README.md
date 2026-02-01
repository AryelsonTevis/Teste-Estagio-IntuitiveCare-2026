# 📊 Projeto 3 – Processamento de Dados em Python

## 📌 Descrição
Projeto desenvolvido em **Python** para processamento, organização e análise de dados relacionados a **despesas e planos de saúde**.  
O sistema lê arquivos CSV, cria tabelas, insere dados e disponibiliza endpoints para consulta.

---

## 🗂️ Estrutura do Projeto

```
projeto3/
│
├── data/
│ └── csv/
│ ├── dados_trimestres_concatenados.csv
│ ├── despesas_agregadas.csv
│ └── planos_de_saude_ativos.csv
│
├── src/
│ ├── main.py
│ ├── criar_tabelas.py
│ ├── inserir_dados.py
│ ├── deletar.py
│ └── endpoints.py
│
└── README.md
```
---
## ⚙️ Funcionalidades
- 📥 Leitura e processamento de arquivos CSV  
- 🗄️ Criação e exclusão de tabelas
- ➕ Inserção de dados no banco
- 🌐 Disponibilização de endpoints para consulta
- 📊 Organização e agregação de despesas

---

## 🛠️ Tecnologias Utilizadas
- Python 3.x  
- Pandas  
- Requests  
- SQLite (ou outro banco, se aplicável)

---

## 📦 Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- `requests`
- `pandas`
- `sqlalchemy`
---
## ▶️ Como Executar o Projeto

1️⃣ Acesse a pasta do projeto
cd projeto3

2️⃣ Instale as dependências
pip install pandas requests sqlalchemy


3️⃣ Execute o projeto
python src/main.py ou py src/main.py