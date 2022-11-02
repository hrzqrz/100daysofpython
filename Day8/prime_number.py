
import numbers


print('This program show that the number is prime or not.')
number = int(input('Enter the number here: '))

def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print(f'The number {num} is Prime Number.')
    else:
        print(f'The number {num} is not Prime Number.')
            
is_prime(number)