Desafio Técnico - Desenvolvedor Python | C2S
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org)

Este projeto implementa um **agente virtual de busca de veículos v1.0**, desenvolvido em Python, atualmente suporta:  
- Modelagem de dados (veículos) via ORM.  
- Banco de dados para persistência local.  
- Comunicação cliente-servidor baseada em protocolo MCP (Model Context Protocol) com sockets TCP.  
- Interface de terminal (CLI) com agente interpretativo de linguagem natural simples.  
- Testes automatizados com para garantir qualidade de código e integridade do fluxo.

Tecnologias Utilizadas:
- Python 3.11
- SQLAlchemy 2.0
- SQLite
- Comunicação Cliente/Servidor via MCP
- Faker para geração de dados ficticios
- Parser de linguagem natural simples para filtros
- Testes automatizados com pytest

[-] Instalação
-


1. Clonar repositório:
```bash
git clone https://github.com/SwintexD/C2S--Desafio-Tecnico.git
cd C2S--Desafio-Tecnico
```

2. Criar e ativar virtualenv (recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Instalar dependências:
```bash
pip install -r requirements.txt
```
[-] Banco de Dados
- O projeto usa SQLite (produtos.db). As tabelas são criadas automaticamente ao rodar 'server.py' ou pelo script de criação inicial.

[-] Como Rodar MCP 

-  Servidor
```bash
python server.py
```
- Cliente/Agente Virtual (Executar em terminal separado)

```bash
python client.py
```

- Testes Automatizados
```bash
test_parser.py → validações da função que interpreta o texto do usuário

test_query_engine.py → valida busca/filtros no DB(produtos.db)

test_integrado.py → valida fluxo Cliente <-> Servidor <-> DB

Para rodar todos os testes use:
pytest -vv
```

- Vídeo Demo
link: 

Observações
-
Considere que, esse projeto é para fins de Desafio Técnico de um sistema simples!!

A quantidade de veículos visualizáveis é configurável, por padrão é '10'

Atualmente o agente entende múltiplos filtros e retorna resultados similares!
```bash
- ex: Gostaria de visualizar uma Ford Ranger Diesel, preferencialmente gostaria de cor preta
- ex: Mostre carros Volkswagen azul automático e flex

```

 O projeto segue boas práticas de Python, organização de código e testabilidade.

 Parser e query engine são separados para facilitar manutenção e testes.

 O código é claro e legível, pronto para execução em qualquer ambiente local desde que siga as etapas acima.
