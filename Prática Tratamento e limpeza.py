# %%
import pandas as pd
import seaborn as sbr
import statistics as sts

# %%
#Importar dados
dataset = pd.read_csv("Churn.csv", sep=";")
#Tamanho
print(dataset.shape)
#Nomeando as colunas
dataset.columns = ["Id","Score","Estado","Gênero","Idade","Patrimônio","Saldo","Produtos","TemCartCrédito","Ativo","Salário","Saiu"]
#Visualizar
print(dataset.head())

# %%
#Explorando dados categóricos e numéricos a procura de erros nos dados para que possamos os tratar e utilizar os dados
#Vulgo boa parte do trabalho de um cientista de dados, pegar os dados, tratar e os transformar em informação
#Estado
agrupado = dataset.groupby(['Estado']).size()
#print(agrupado)
agrupado.plot.bar(color = 'red')

# %%
#Gênero
agrupado = dataset.groupby(['Gênero']).size()
print(agrupado)
agrupado.plot.bar(color = 'blue')

# %%
#Score
dataset['Score'].describe()
#Boxplot
sbr.boxplot(dataset['Score']).set_title('Score')
#Histograma
sbr.histplot(dataset['Score']).set_title('Score')

# %%
#Idade
dataset['Idade'].describe()
#Boxplot
sbr.boxplot(dataset['Idade']).set_title('Idade')
#Histograma
sbr.histplot(dataset['Idade']).set_title('Idade')

# %%
#Saldo
print(dataset['Saldo'].describe())
#Boxplot
sbr.boxplot(dataset['Saldo']).set_title('Saldo')
#Histograma
sbr.histplot(dataset['Saldo']).set_title('Saldo')

# %%
#Salário
print(dataset['Salário'].describe())
#Boxplot
sbr.boxplot(dataset['Salário']).set_title('Salário')
#Histograma
sbr.histplot(dataset['Salário']).set_title('Salário')

# %%
#Início do tratamento dos dados, verificando se há valores NAN

print(dataset.isnull().sum())

#Localizados em Salário(7) e Gênero(8)

# %%
#Tratando os valores NAN em salário

mediSal = sts.median(dataset['Salário'])
dataset['Salário'].fillna(mediSal, inplace=True)
print(dataset['Salário'].isnull().sum())

# %%
#Tratando os valores NAN em Gênero

#Primeiro preencher os valores NAN com a moda, nesse caso o Masculino
dataset['Gênero'].fillna('Masculino', inplace=True)
#print(dataset['Gênero'].isnull().sum())
#Agora modificando os valores incorretos na coluna de gênero
dataset.loc[dataset['Gênero'] == 'M', 'Gênero'] = "Masculino"
dataset.loc[dataset['Gênero'].isin(['Fem','F']), 'Gênero'] = "Feminino"
agrupado = dataset.groupby(['Gênero']).size()
print(agrupado)

# %%
#Tratamento dos dados da idade

#Averiguando se há dados fora do domínio
dataset['Idade'].describe()
#Temos idades negativas e maiores que 120 anos, agora precisamos localizar essas idades
dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120)]
#Encontrado os valores vamos substituilos pela mediana das idades
meanIda = sts.median(dataset['Idade'])
dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120), 'Idade'] = meanIda

# %%
#Agora verificação de duplicata de dados
#Como temos o identificador único Id neste conjunto de dados podemos facilmente identificar e resolver este problema
dataset[dataset.duplicated(['Id'],keep=False)]
#Averiguando uma duplicação partimos para a deleção da duplicata
dataset.drop_duplicates(subset='Id',keep='first',inplace=True)

# %%
#Tratamento de dados de Estado

#Verificando se há dados forad e domínio
groupEs = dataset.groupby(['Estado']).size()
#Averiguando que há valores fora do domínio atribuimos a moda a esses valores
dataset.loc[dataset['Estado'].isin(['TD','SP','RP']), 'Estado'] = "RS"
groupEs

# %%
#Por fim averiguar os outliers na coluna Salário, vamos considerar os acima de dois desvios padrão
desv_p = sts.stdev(dataset['Salário'])
#Averiguar se algum valor atende ao critério
dataset.loc[dataset['Salário'] >= 2 * desv_p]
#Encontrando os valores acima do desvio agora é subtituir mais uma vez pela mediana
meanSal = sts.median(dataset['Salário'])
dataset.loc[dataset['Salário'] >= 2 * desv_p] = meanSal

# %%
print(dataset.head())
dataset.shape


