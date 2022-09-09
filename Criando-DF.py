import pandas as pd

data = pd.read_csv('winemag-data_first150k.csv', index_col=0)

indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cols = ['country', 'province', 'region_1', 'region_2']
df = data.loc[indices, cols]
df