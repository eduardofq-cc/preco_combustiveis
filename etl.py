from db_engine import conector
import pandas as pd

#Extração - importaçao da base de dados.
df = pd.read_csv('dados/precos_semestrais_automotivos_2024_02.csv', sep=';')

#Transformação - tratamento dos dados.

#Renomear colunas.
dc_colunas = {
    "Regiao - Sigla":"regiao_sigla",
    "Estado - Sigla":"estado_sigla",
    "Municipio":"municipio",
    "Revenda":"revenda",
    "CNPJ da Revenda":"revenda_cnpj",
    "Nome da Rua":"endereco_rua_nome",
    "Numero Rua":"endereco_rua_numero",
    "Complemento":"endereco_complemento",
    "Bairro":"endereco_bairro",
    "Cep":"endereco_cep",
    "Produto":"produto",
    "Data da Coleta":"coleta_data",
    "Valor de Venda":"valor_venda",
    "Valor de Compra":"valor_compra",
    "Unidade de Medida":"medida_unidade",
    "Bandeira":"bandeira"}
df.rename(columns = dc_colunas, inplace=True)

#Ajustar o formato de data.
df['coleta_data'] = pd.to_datetime(df['coleta_data'], dayfirst=True)

#Ajustar valores numéricos.
df['valor_venda'] = df['valor_venda'].str.replace(',','.').astype(float)

#Remover espaços internos da unidade de medida.
df['medida_unidade'] = df['medida_unidade'].str.replace(' ', '')

#Load - carregamento dos dados para o banco de dados sqlite.

#Conector e engine para comunicação com o banco de dados.
db = conector('db/base.db')
engine = db.get_engine()

#Enviar informações para o banco de dados.
df.to_sql('precos_combustiveis', con=engine, if_exists='replace', index=False)