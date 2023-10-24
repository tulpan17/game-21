import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def calculate_score(hand):
    return sum(hand)

player_hand = [random.choice(deck)]
deck.remove(player_hand[0]) 
player_score = calculate_score(player_hand)

computer_hand = [random.choice(deck)]
deck.remove(computer_hand[0])
computer_score = calculate_score(computer_hand)
