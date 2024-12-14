# print('Zaczynamy')

# age = input('Ile masz lat? ')

# try:
#     age = int(age)
# except:
#     print('przyjmuje wiek 10 lat')
#     age = 10
    
# print(f'bedziesz dorosly za {18 - age} lat')




# result = a / b

# while True:
#     try:
#         a = int(input('podaj dzielna: '))
#         b =  int(input('podaj dzielnik: '))
#         break
#     except:
#         print('zla wartosc, jeszcze raz')
# print('dalej')

try:
    a = int(input('podaj dzielna: '))
    b = int(input('podaj dzielnik: '))
    result = a / b
    print('piesek'[6])
except ValueError:
    print('nie da się przeksztalcic danej wejsciowej na int')
except IndexError:
    print('za daleko w indeksach')
except ZeroDivisionError:
    print('dzielnik jest 0')
    raise