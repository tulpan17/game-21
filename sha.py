import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def calculate_score(hand):
    return sum(hand)

player_hand = [random.choice(deck)]  # Добавляем одну известную карту игроку
deck.remove(player_hand[0])  # Удаляем выбранную карту из колоды
player_score = calculate_score(player_hand)

computer_hand = [random.choice(deck)]  # Добавляем одну известную карту компьютеру
deck.remove(computer_hand[0])  # Удаляем выбранную карту из колоды
computer_score = calculate_score(computer_hand)

next_turn = "player"


for i in range(5):
    if next_turn == "player":

        if player_score < 21:
            action = input("Ваш ход. Хотите взять карту? (да/нет): ").lower()
            if action == "да":
                card = random.choice(deck)
                player_hand.append(card)
                player_score = calculate_score(player_hand)
                print(f"Вы взяли карту: {card} (ваш счет: {player_score})")
                deck.remove(card)  # Удалить выбранную карту из колоды
            else:
                print("Вы пропускаете ход.")
            next_turn = "computer"
        else:
            next_turn = "computer"

    elif next_turn == "computer":
        