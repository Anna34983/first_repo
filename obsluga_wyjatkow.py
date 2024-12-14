data = input('Wprowadz dana: ')
try:
    data = int(data)
    print(f'{data} jest intem\n{type(data)}')
except:
    data = float(data)
    print(f'{data} jest floatem\n{type(data)}')
except:
    print(f'{data} jest stringiem\n{type(data)}')