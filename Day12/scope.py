#global scope are available within the functions and also outside the functions
enemies = 1

#local scope
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")

