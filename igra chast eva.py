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
