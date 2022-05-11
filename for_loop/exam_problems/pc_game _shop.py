sold_games = int(input())
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
other_counter = 0

for numbers in range(sold_games):
    game = input()
    if game == "Hearthstone":
        hearthstone_counter += 1
    elif game == "Fornite":
        fornite_counter += 1
    elif game == "Overwatch":
        overwatch_counter += 1
    else:
        other_counter += 1

all_games = hearthstone_counter + fornite_counter + overwatch_counter + other_counter
hearthstone_percent = hearthstone_counter / all_games * 100
fornite_percent = fornite_counter / all_games * 100
overwatch_percent = overwatch_counter / all_games * 100
other_percent = other_counter / all_games * 100
print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {other_percent:.2f}%")









