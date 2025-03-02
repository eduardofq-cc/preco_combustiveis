# Visão geral do projeto
O projeto consiste em disponibilizar informações referentes a preços de combustíveis dos diversos estados brasileiros em um banco de dados SQLite para análise. Os dados são tratados antes de serem carregados para o banco de dados.

## Fonte dos dados
Os dados utilizados neste projeto são disponibilizados pela [ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis)](https://www.gov.br/anp/pt-br) por meio do [LPC (Levantamento de Preços de Combustíveis)](https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/precos-revenda-e-de-distribuicao-combustiveis/informacoes-levantamento-de-precos-de-combustiveis), em cumprimento às determinasções da Lei do Petróleo (Lei nº 9478/1997), realizado semanalmente em 459 localidades por empresa contratada.


Os dados são disponibilizados no [Portal Brasileiro de Dados Abertos e Catálogo Nacional de Dados](https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp), extratificados por semestre.

## Atividades do projeto
No desenvolvimento do projeto foram realizadas as seguintes atividades em ordem cronológica:

1. Instalação do VSCode e suas extensões para Python, Jupyter Notebook, Git e GitHub;
2. Criação do repositório do projeto com sua estrutura de diretórios no GitHub e e sincronização com o Git local;
3. Criação de um ambiente virtual e instalação das bibliotecas Python já citadas;
4. Download do [conjunto de dados](https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp) referente ao segundo semestre de 2024;
5. Criação de dois notebooks Jupyter, um para exploração inicial dos dados e outro para análise, demonstrando ao final  o município de Minas Gerais com o preço de venda mais barato;
6. Criação de um banco de dados SQLite, já instalado por padrão na distribuição Ubuntu do Linux.
7. Criação de um objeto Python para conexão com o banco de dados, com retorno de uma engine a ser utilizada pela biblioteca Pandas do Python.
8. Criação de um código em Python para ETL (Extract, Transform, Load) dos dados, persistindo os dados no banco de dados do projeto.

## Estrutura de diretórios e arquivos
    preco_combustiveis
    |- .venv
       (arquivos de pacotes instalados)
    |- dados
       |- metadados-serie-historica-precos-combustiveis.pdf
       |- precos_semestrais_automotivos_2024_02.csv
    |- db
       |- base.db
       |- create_precos_combustiveis.sql
    |- analise.ipynb
    |- db_engine.py
    |- etl.py
    |- explorar.ipynb
    |- README.md


A raíz do projeto contém 5 arquivos:
- `README.md` é este arquivo, com informações sobre o projeto.
- `explorar.ipynb` e `analise.ipynb` são notebooks Jupyter que apresentam, respectivamente, uma exploração inicial e uma análise dos dados do arquivo `precos_semestrais_automotivos_2024_02.csv`, do diretório `dados`.
- `db_engine.py` contém um código em Python de uma classe responsável pela conexão com o banco de dados SQLite, utilizando a biblioteca `SQLAlchemy`.
- `etl.py` contém um código em Python para ETL (Extract, Transform, Load) dos dados. Os dados são extraídos de um arquivo `.csv`, tratados e carregados no banco de dados SQLite `base.db`, no diretório `db` .


O diretório `.venv` é o diretório do ambiente virtual, contendo diversos arquivos dos pacotes Python instalados e usados no projeto.

O diretório `dados` contém 2 arquivos:
- `precos_semestrais_automotivos_2024_02.csv` contém os dados no formato `.csv`.
- `metadados-serie-historica-precos-combustiveis.pdf` contém as informações sobre os dados contidos no arquivo `precos_semestrais_automotivos_2024_02.csv`.

O diretório `db` contém 2 arquivos:
- `base.db` é o banco de dados SQLite para onde são enviados os dados tratados.
- `create_precos_combustiveis.sql` contém o código SQL para criação da tabela "precos_combustiveis" no banco de dados `base.db`.

## Recursos utilizados

**Linguagens**
- [Python](https://www.python.org/);
- [SQL](https://www.w3schools.com/sql/);
- [Markdown](https://www.markdownguide.org/).

**Bibliotecas Python**
- [Pandas](https://pandas.pydata.org/);
- [Matplotlib](https://matplotlib.org/);
- [SQLAlchemy](https://www.sqlalchemy.org/).

**Sistemas de controle de versão**
- [Git](https://git-scm.com/);
- [GitHub](https://github.com/).

**Banco de dados**
- [SQLite](https://www.sqlite.org/index.html).

**IDE**
- [VSCode](https://code.visualstudio.com/).

**Sistema Operacional**
- [Linux Ubuntu](https://ubuntu.com/desktop).