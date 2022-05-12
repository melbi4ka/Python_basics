game_days = int(input())
win_days = 0
lose_days = 0
total_reward = 0

for numbers in range(game_days):
    comand = input()
    win_game_counter = 0
    lost_game_counter = 0
    day_reward = 0

    while comand != "Finish":
        sport = comand
        sport_result = input()

        if sport_result == "win":
            day_reward += 20
            win_game_counter += 1
        elif sport_result == "lose":
            day_reward += 0
            lost_game_counter += 1
        comand = input()

    if win_game_counter > lost_game_counter:
        day_reward *= 1.1
        win_days += 1
    else:
        lose_days += 1
    total_reward += day_reward

if win_days > lose_days:
   print(f"You won the tournament! Total raised money: {total_reward*1.2:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_reward:.2f}")
