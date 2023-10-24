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