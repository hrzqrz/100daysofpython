from unicodedata import name


def greet_with(name, location):
    print(f'Hello, {name}')
    print(f'Where are you from {name} ?')
    print(f'{name}: i am form {location}')
    
greet_with('roza', 'Bandar_e_abbas')