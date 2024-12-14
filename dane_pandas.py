# import pandas as pd

# import time

#from time import * wtedy nie muszę podawać nazwy biblioteki, czyli time.sleep

# import time # inne wywołanie biblioteki

# print('piesek spi')
# time.sleep(2)
# print('piesek wstal')

import pandas as pd

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