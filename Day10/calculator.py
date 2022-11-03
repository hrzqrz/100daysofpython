def add(n1, n2):
    """ This function add 2 numbers."""
    return n1 + n2

def subtract(n1, n2):
    """This function subtract n1 - n2"""
    return n1 - n2

def multiple(n1, n2):
    """This function multiple n1 in n2"""
    return n1 * n2

def divide(n1, n2):
    """This function divide n1 by n2."""
    return n1 / n2

operations = {'+': add,
              '-': subtract,
              '*': multiple,
              '/': divide
              }
num1 = int(input('Whats the first number : '))

for symbol in operations:
    print(symbol)
    
operation_symbol = input('Pick an operation from the line above: ')

num2 = int(input('Whats the second number : '))

calculate_function = operations[operation_symbol]
result = calculate_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")
 