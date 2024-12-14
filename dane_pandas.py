# import pandas as pd

# import time

#from time import * wtedy nie muszę podawać nazwy biblioteki, czyli time.sleep

# import time # inne wywołanie biblioteki

# print('piesek spi')
# time.sleep(2)
# print('piesek wstal')

import pandas as pd
import numpy as np

df = pd.read_csv('diabetes.csv')
print(df)

print(type(df))

print(f'ilosc danych: {df.shape}') #wynikiem jest lista dwuelementowa, wskazująca liczbę wierszy i kolumn

print(f'wypisuje wszystko:\n{df}')
print(f'wypisuje typ:\n typ(df)')
print(f'ilosc danych: {df.shape}\n liczba kolumn: {df.shape[1]}')
print(f'wypisuje jak chce:\n{df.to_string()}') #wypisuje wszystko
print(f'wypisuje jak chce:\n{df.head(3).to_string()}') #wypisuje 3 wiersze
print(f'opis danych:\n{df.describe()}')
print(f'opis danych:\n{df.describe().T.to_string()}') # T - zamian wierszy z kolumnami
print(f'ilosc pustych pol:\n{df.isna().sum()}')

#wszędzie, gdzie są zera lub brak wartości - wpisz średnią (bez zer)

# df['bmi'] =+ 1000
# df['nowa_testowa'] = df['bmi'] / df['glucose'] - 50 * df.shape[1]
# print(f'opis danych:\n{df.describe().T.to_string()}')

# df[bmi] = df['bmi'].replace(0,np.nan) # zamieniamy zera na brak wartości

for col in ['glucose','bloodpressure','skinthickness','insulin','bmi','diabetespedigreefunction','age']:
    df[col].replace(0,np.nan,inplace=True) #usuwamy zera
    mean_ =df[col].mean() #liczymy srednia
    df[col].replace(np.nan, mean_,inplace=True) #wpisujemy srednią tam gdzie puste wartości
    
print('po czyszczeniu')
print(df.describe().T.to_string())
print(df.isna().sum()) # suma pustych pol
          
# df.to_csv(r'..\cukrzyca.csv')
df.to_csv('cukrzyca.csv')    