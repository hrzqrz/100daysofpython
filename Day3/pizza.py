from re import S


print('welcome to python pizza deliveries.')
size = input('What size pizza do you want? s, m or l: ')
add_pepperoni = input('Do you want pepperoni? y or n: ')
extre_cheese = input('Do you want extra cheese? y or n: ')

bill = 0

if size == 's':
    bill = 15
elif size == 'm':
    bill = 20 
elif size == 'l':
    bill = 25
if add_pepperoni == 'y':
    bill += 5
if extre_cheese == 'y':
    bill += 3
else:
    print('Choose a size for your pizza')
print(f'your bill is: {bill}')
    