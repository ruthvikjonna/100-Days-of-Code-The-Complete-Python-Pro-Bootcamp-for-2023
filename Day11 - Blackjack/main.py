import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    """Takes a list of cards and returns the score calculated"""
    score = sum(card_list)
    if (11 in card_list) and (score > 21):
        index_11 = card_list.index(11)
        card_list[index_11] = 1
    return score

def compare(user_score, computer_score):
    '''Takes the user's score and computer's score, compares them, and returns the game result'''
    if user_score > 21 and computer_score > 21:
        return "\nYou went over 21. You lose."
    if user_score == computer_score:
        return "\nGame over. It's a draw."
    elif computer_score == 21:
        return "\nGame over. You lose."
    elif user_score == 21:
        return "\nBlackjack! You win!"
    elif user_score > 21:
        return "\nYou went over 21. You lose."
    elif computer_score > 21:
        return "\nDealer went over 21! You win!"
    elif user_score > computer_score:
        return "\nGame over! You win!"
    elif computer_score > user_score:
        return "\nGame over. You lose."

user_cards = []
computer_cards = []

def play_game():

    for i in range(1, 5):
        value = deal_card()
        if i == 1 or i == 3:
            user_cards.append(value)
        elif i == 2 or i == 4:
            computer_cards.append(value)

    game_over = False
    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}")
        print(f"Dealer's first card: {computer_cards[0]}\n")
        print(f"Your score: {user_score}")
        print(f"Dealer's score: {computer_cards[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_over = True
        else:
            draw_another = input("\nWould you like to draw another card? Type 'yes' to draw, 'no' to pass: ")
            if draw_another == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print()
    print("---------------------------------------------")
    print(f"\nYour final hand: {user_cards}")
    print(f"Dealer's final hand: {computer_cards}\n")
    print(f"Your final score: {user_score}")
    print(f"Dealer's final score: {computer_score}")
    print(compare(user_score, computer_score))

print(logo)
print("Welcome to Blackjack!")
play_game()