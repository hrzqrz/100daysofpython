height = int(input('Enter your height in CM:'))

bill = 0
if height > 120:
    print('you can ride .')
    age = int(input('Enter your age:'))
    if age < 12:
        bill = 5
    elif  age <= 18:
        bill = 7
    else:
        bill = 12
    wnats_photo = input('do you want a photo taken? Y of N.')
    if wnats_photo == 'y':
        bill += 3
    print(f'your final bill is: {bill}')
else:
    print('Cant ride')