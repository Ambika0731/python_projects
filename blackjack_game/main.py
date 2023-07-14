
from os import system, name
from art import logo
import random

# define clear function
def clear():
    # for mac and linux os name is posix
    if name == 'posix':
        _ = system('clear')
    # for windows os name is nt
    else:
        _ = system('cls')

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    
    while not is_game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print(f"Your cards:{user_cards}, current score: {user_score}" )
        print(f"Computer's first card:{computer_cards[0]}")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    
    clear()
    # or we can directly clear the screen using
    # os.system('clear')

    play_game()
