# Projeto 1 – Processamento de Arquivos

## 📌 Descrição
Este projeto tem como objetivo realizar o processamento automático de arquivos de diferentes formatos (CSV, TXT, XLSX), extraindo, normalizando e organizando dados de forma padronizada para análise posterior.

O sistema identifica automaticamente a estrutura dos arquivos e trata variações de colunas e formatos, garantindo consistência nos dados finais.

---

## 🚀 Funcionalidades
- 📂 Leitura automática de arquivos ZIP
- 🗜️ Extração de arquivos compactados
- 📄 Suporte a múltiplos formatos (CSV, TXT, XLSX)
- 🔍 Identificação dinâmica de colunas
- 🔄 Normalização de dados
- 📊 Preparação dos dados para análise ou exportação

---

## 🛠️ Tecnologias Utilizadas
- Python 3.x  
- Bibliotecas padrão do Python  
- Pandas (se aplicável)  
- OpenPyXL (para arquivos Excel)

---

## 📁 Estrutura do Projeto
projeto1/
│
├── data/ # Arquivos de entrada
├── output/ # Arquivos processados
├── src/ # Código-fonte
│ └── main.py
├── requirements.txt # Dependências
└── README.md

1️⃣ Acesse a pasta do projeto
cd projeto1

2️⃣ Instale as dependências
pip install pandas requests


3️⃣ Execute o projeto
python src/main.py ou py src/main.py