
import imp
import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =  random.choice(cards)
    return card 

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards) 
def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw '
    elif computer_score == 0:
        return 'Lose, opponent has BlackJack'
    elif user_score == 0:
        return 'Win with a BlackJack'
    elif user_score > 21:
        return 'You went over, You lose'
    elif computer_score > 21:
        return 'Opponent went over. you win'
    elif user_score > computer_score:
        return 'You win'
    else:
        return 'You lose'
    
def paly_game():  
    print(logo)  
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(user_cards)   


    print(calculate_score(user_cards))
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user cards are: {user_cards} and user score is: {user_score}")
        print(f"The computer first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n'") == 'y':
    paly_game()
    