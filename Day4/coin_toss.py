import random
print('Coin toss Game')
random_side = random.randint(0, 1)

if random_side == 1:
    print('Heads')
else:
    print('Tails')