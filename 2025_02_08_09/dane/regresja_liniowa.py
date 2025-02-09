import pandas as pd

df = pd.read_csv('dane\\weight-height.csv')
print(df.head(10))
print(df.Gender.value_counts())
df.Height *= 2.54
df.Weight /= 2.2
print(f'Po zmianie jednostek: \n{df.head(10)}')