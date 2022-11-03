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

def calculation():
    num1 = int(input('Whats the first number : '))

    for symbol in operations:
        print(symbol)
        
    end_of_calculation = True    
    while end_of_calculation:    
        operation_symbol = input('Pick an operation : ')

        num2 = int(input('Whats the nest number? : '))

        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        user_answer = input(f'Type y to continue calculation with {answer}, or type n to start a new calculation.: ').lower()
        if user_answer == 'y':
            num1 = answer
        else:
            end_of_calculation = False
            print(f"The final answer is: {answer}")
            print('Goood CAlculation.')
            calculation()
            
calculation()
            
 