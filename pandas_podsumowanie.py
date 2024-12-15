import pandas as pd
df = pd.read_csv(diabetes.csv)
df_excel = pd.read_excel('plik.xlsx', sheet_name='Arkusz1')

df.head()                   # domyślnie wyświetla 5 pierwszych wierszy
df.head(10)                 # wyświetla 10 pierwszych wierszy

df.tail()                   # domyślnie wyświetla 5 ostatnich wierszy
df.tail(10)                 # wyświetla 10 ostatnich wierszy

df.info()                   # Wyświetla liczbę wierszy, kolumn, typy danych oraz liczbę niepustych rekordów w każdej kolumnie

df.describe()               # Opis statyczny

df['nazwa_kolumny']         # zwraca series z danej kolumny
df[['kolumna1','kolumna2']] # zwraca DataFrame z wybranych kolumn

df[df['kolumna'] == 'wartosc']
df[df['kolumna'] > 10]
df[(df['kolumna1'] > 5) & (df['kolumna1'] == 'abc')]

df.loc[0:10, ['kolumna1','kolumna2']]   # wiersze od 0 do 10, tylko dwie kolumny
df.iloc[0:10, 0:2]                      # wiersze od 0 do 10, kolumny od 0 do 2

df['kolumna_numeryczna'].sum()
df.sum()    # domyslnie wykona sume dla każdej kolumny numerycznej
df['kolumna'].count()   # zwraca liczbę niepustych (nie NaN) wartosci w kolumnie
df.count()
df['kolumna_numeryczna'].mean()
df['kolumna_numeryczna'].median()
df['kolumna_numeryczna'].std()
df['kolumna_numeryczna'].unique()   # Lista unikalnych wartosci
df['kolumna_numeryczna'].unique()   # Liczba unikalnych wartosci

grupa = df.groupby('kolumna_kategoryczna')
grupa['kolumna_numeryczna'].mean()
# zwraca srednie wartosci kolumny numerycznej w podziale na unikalne wartosci w kolumnie kategorycznej

df.groupby('kolumna_kategoryczna')