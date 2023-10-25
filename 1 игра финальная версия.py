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


next_turn = "player"
for i in range(5):
    print(f"Ваши карты: {player_hand} (счет: {player_score})")
    print(f"Карты компьютера: {computer_hand[1:]}")
    if next_turn == "player":
        if player_score < 21:
            action = input("Ваш ход. Хотите взять карту? (да/нет): ").lower()
            if action == "да":
                card = random.choice(deck)
                player_hand.append(card)
                player_score = calculate_score(player_hand)
                print(f"Вы взяли карту: {card} (ваш счет: {player_score})")
                deck.remove(card)
            else:
                print("Вы пропускаете ход.")
            next_turn = "computer"
        else:
            next_turn = "computer"

    elif next_turn == "computer":
        if computer_score < 21:
            if computer_score < 17:
                card = random.choice(deck)
                computer_hand.append(card)
                computer_score = calculate_score(computer_hand)
                if i > 0: 
                    print(f"Компьютер взял карту: {card}")
                deck.remove(card) 
            else:
                print("Компьютер пропускает ход.")
            next_turn = "player"
        else:
            next_turn = "player"

    if player_score == 21:
        print("Поздравляем, вы счастливчик! Ровно 21 очко!")
        break
    elif computer_score == 21:
        print("Блин.. но ничего, у вас есть еще пальцы!")
        break

if i == 4:
    print("Игра завершена. У вас и компьютера больше нет ходов.")
    if player_score <= 21 and (computer_score > 21 or player_score > computer_score):
        print("Удача на вашей стороне!")
    elif computer_score <= 21 and (player_score > 21 or computer_score > player_score):
        print("Упс! На следующей лавке (Замена пальцев) скидка для вас!")
    elif player_score == computer_score:
        print("Ничья!")
    else:
        print("Нет победителя. Значит проиграли оба!")
        
print(f"Ваши карты: {player_hand} (счет: {player_score})")
print(f"Карты компьютера: {computer_hand[1:]} (счет компьютера: {computer_score})")
