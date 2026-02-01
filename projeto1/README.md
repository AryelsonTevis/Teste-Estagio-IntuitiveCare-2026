# 📊 Projeto – Processamento de Dados da ANS

## 📌 Descrição
Este projeto realiza o **download, extração, processamento e consolidação de dados públicos da ANS (Agência Nacional de Saúde Suplementar)** referentes às demonstrações contábeis trimestrais e à lista de operadoras de planos de saúde ativas.

Ao final do processo, os dados são filtrados, normalizados, convertidos em CSV e compactados em um arquivo `.zip`.

---

## 📁 Estrutura do Projeto



```
projeto1/
│
├── src/
│ ├── main.py
│ ├── endpoints.py
│ ├── extrair.py
│ ├── detectar.py
│ ├── criar_csv.py
│ └── compactar_para_zip.py
│
├── data/
│ ├── zip/
│ └── csv/
│
└── README.md
```
---

## ⚙️ Funcionalidades

- Download dos arquivos ZIP dos últimos trimestres disponíveis
- Download da lista de operadoras de planos de saúde ativas
- Extração automática dos arquivos ZIP
- Detecção e filtragem dos dados relevantes
- Formatação e normalização dos valores
- Geração de arquivo CSV final
- Compactação do resultado em um arquivo ZIP

---

## 📦 Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- `requests`
- `pandas`
---
## ▶️ Como Executar o Projeto
1️⃣ Acesse a pasta do projeto
cd projeto1

2️⃣ Instale as dependências
pip install pandas requests


3️⃣ Execute o projeto
python src/main.py ou py src/main.py