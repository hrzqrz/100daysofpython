total = 0 
even_numbers = []
for num in range(1, 101):
    if num % 2 == 0 :
        total += num
        even_numbers.append(num)
print('Even numbers: ')
print(even_numbers)
print(f'The sum of even numbers is {total}')