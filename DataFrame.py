import pandas as pd

fruits = pd.DataFrame([[30, 21]], columns=['Maçãs', 'Bananas'])

fruits_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Maçãs', 'Bananas'], index=['2017 Sales', '2018 Sales'])

quantidades = ['4 cups', '1 cup', '2 large', '1 can']
itens = [ 'Flour', 'Leite', 'Ovos', 'Arroz']
receita = pd.Series(quantidades, index=itens, name='Cozinha')

receita.to_csv('Receita-bolo.csv')
receita

# VINHOS

reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)
reviews.country
reviews['country'] # Usando dicionario para evitar palavras reservadas
reviews['country'][1]

# Seleção baseada em indice -iloc- primeiro linha dps coluna
reviews.iloc[1]
# obtendo coluna
reviews.iloc[:, 1] # " : " significa tudo em python
reviews.iloc[:3, 0] # selecionando as 3 primeiras linhas
reviews.iloc[1:3, 0]
reviews.iloc[[0, 1, 2], 0] # passando uma lista   ILOC EXCLUI O ULTIMO

# de tras p frente
reviews.iloc[-5:] # pegando as ultimas 5 linhas

# Seleção baseada em loc, valor dos dados que importa
reviews.loc[1, 'country']
# situações onde é mais facil usar o loc
reviews.loc[:, ['country', 'points', 'price']] # todas linhas das colunas x
reviews.set_index('title')
reviews.country == 'Italy' # resulta em True/False (booleano)
reviews.loc[reviews.country == 'Italy']
# procurando pelos melhores vinhos
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
# apenas vinhos que sejam da Italia ou da França
reviews.loc[reviews.country.isin(['Italy', 'France'])] # .is in
# tirando os vinhos que estao sem preço
reviews.loc[reviews.price.notnull()]

# atribuindo dados
reviews['critic'] = 'everyone'
reviews['critic']
# iteravel de valor
reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']
# buscando valores especificos
indices = [1, 2, 3, 5, 8] # declarar indice primeiro
sample_reviews = reviews.loc[indices]
