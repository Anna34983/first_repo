import pandas as pd

# wczytywanie danych
df = pd.read_json('dane\dane.json')
print(df)

# wyświetlanie danych
print("\n pierwsze 5 wierszy danych")
print(df.head())

# filtrowanie danych
mlodsi_niz_30 = df[df["wiek"] < 30]
print("\nOsoby mlodsze niz 30lat:")
print(mlodsi_niz_30)