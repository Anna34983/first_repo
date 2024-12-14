print('Zaczynamy')

age = input('Ile masz lat? ')

try:
    age = int(age)
except:
    print('przyjmuje wiek 10 lat')
    age = 10
    
print(f'bedziesz dorosly za {18 - age} lat')