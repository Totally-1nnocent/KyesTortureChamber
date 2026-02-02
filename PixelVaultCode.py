import pandas as pd

df = pd.read_csv('pixelvault game sales.csv')

#print(df.head())
#print(df.tail())
#print(df.shape)

#print(df.columns)
#print(df.info())

#print(df[df.isna()])
#print(df[df.duplicated()])
#print(df[df['total_sale'] != (df['price'] * df['quantity'])])

#print(df.describe())
#print(df['game_title'].value_counts(ascending=True).head(1))
#print(df['category'].value_counts().tail(1))

minidf = df[df['category'] == 'Simulation']
print(minidf.head())