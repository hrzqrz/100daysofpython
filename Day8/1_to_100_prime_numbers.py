print('This program find the prime numbers bitween 1 and 100.')

def prime_numbers():
    prims = []
    none_primes = []
    
    for i in range(1, 101):
        num = i
        is_prime = True
        if num == 1 :
            prims.append(num)
        else:
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
        if is_prime:
            prims.append(num)
        else:
            none_primes.append(num)
    print("Prime Numbers: ")
    print(prims)
    print('None prime numbers: ')
    print(none_primes)
    
prime_numbers()