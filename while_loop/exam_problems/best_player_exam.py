current_comand = input()
best_player = ""
hat_trick = False
goal_comparator = 0

while current_comand != "END":
    goals = int(input())
    if goals > goal_comparator:
        goal_comparator = goals
        best_player = current_comand
        if goals >= 3:
            hat_trick = True
            if goals >= 10:
                break
    current_comand = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {goal_comparator} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goal_comparator} goals.")
