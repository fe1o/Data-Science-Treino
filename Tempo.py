# %%
import pandas as pd
import seaborn as sbr
import statistics as sts

# %%
#Projeto com a planilha de tempo com o objetivo de tratar os valores NAs e fora de domínio
#Lendo o arquivo com os dados
data_set = pd.read_csv("tempo.csv", sep=";")
#Vendo forma e cabeçalho da planilha
print(data_set.head())
data_set.shape

# %%
#Começando a tratar os dados pelos valores NAs
data_set.isnull().sum()
#Tratando os valores
vento_g = data_set.groupby(['Vento']).size()
data_set['Vento'].fillna('FALSO',inplace=True)
umidade_g = data_set.groupby(['Umidade']).size()
data_set['Umidade'].fillna(70,inplace=True)
print(data_set.isnull().sum())

# %%
#Buscando valores fora de domínio
#Ap - Sol, Nublado, Chuva
#Temp - -135F ~ 130F
#Umidade -  0 ~ 100
#Jogar - Sim/Não

#Umidade tinha 1 valor de 200
umidade_g
data_set.loc[data_set['Umidade'] == 200, 'Umidade'] = 70

#'Aparencia' sem problemas
apa_g = data_set.groupby(['Aparencia']).size()
apa_g

#Temperatura também com 1 valor fora
temp_g = data_set.groupby(['Temperatura']).size()
data_set.loc[data_set['Temperatura'] == 1220, 'Temperatura'] = 75
temp_g

#Jogar também sem problemas
jog_g = data_set.groupby(['Jogar']).size()
jog_g

# %%
#Dados tratados
apa_g
temp_g
umidade_g
vento_g
jog_g
print(data_set.isnull().sum())


