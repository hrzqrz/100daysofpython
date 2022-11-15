from game_data import data
from game_logo import logo, vs
import random

# format the account into printable format
def format_data(acount):
    """Take the account data and returns the printable format."""
    acount_name = acount['name']
    acount_description = acount['description']
    acount_country = acount['country']
    return f"{acount_name}, a {acount_description}, from {acount_country}"

# use if statement to check if user is correct
def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
game_should_continue = True
# Display art
print(logo)
acount_b = random.choice(data)
while game_should_continue:
    # Generate a random account from the game data.
    # make acount at postition B become the next account at position A
    acount_a = acount_b
    acount_b = random.choice(data)
    while acount_a == acount_b:
        acount_a = random.choice(data)

    print(f"Compare A: {format_data(acount_a)}")
    print(vs)
    print(f"Againset B: {format_data(acount_b)}")
    print()

    # ask user for guess
    guess = input("WHo has more followers? Type 'A' or 'B': ").lower()

    # get follower count of each account
    a_followers_count = acount_a['follower_count']
    b_followers_count = acount_b['follower_count']

    # check if user is correct
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"you're right! Current score: {score}")
    else:
        print(f"Sorry, you're wrong! Final score: {score}")
        game_should_continue = False
    # score keeping

    # make the game repeatable

    

    # clear the screen between rounds 


