import pandas as pd

data = pd.read_csv('winemag-data_first150k.csv', index_col=0)

indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cols = ['country', 'province', 'region_1', 'region_2']
df = data.loc[indices, cols]


cols= ['country', 'variety']
df = data.loc[:99, cols]

# ou
# selecionando por indice
index_cols= [0, 11]
df = data.iloc[:100, index_cols]

# avaliações de vinho na italia
vinhos_italianos = data[data.country == 'Italy']
# melhores vinho da oceania
top_oceania = data.loc[
    (data.country.isin(['Australia', 'New Zealand']))
    & (data.points >= 95)
]