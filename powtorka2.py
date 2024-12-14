# print('Hello')

# input()

age = int(input('Ile masz lat? '))

# print(f'Wiec masz {age} lat') # f oznacza że w nawiasie { masz zmienna
# print(f'Bedziesz dorosly za {18 - age} lat')

while True:
    if 0 < age < 18:
        print(f'wiec masz {age} lat')
        print(f'bedziesz dorosly za {18 - age} lat')
        break
    else:
        print('zly wiek')
        break
print('Dalsza czesc programu')