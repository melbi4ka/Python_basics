name = input()
games = int(input())
is_play = False
points = 0
w_counter = 0
d_counter = 0
l_counter = 0


for numbers in range(1, games+1):
    result = input()
    if numbers < 1:
        is_play = False
    if numbers >= 1:
        is_play = True
        if result == "W":
            points += 3
            w_counter += 1
        elif result == "D":
            points += 1
            d_counter += 1
        elif result == "L":
            points += 0
            l_counter += 1
all_counter = w_counter + d_counter + l_counter
if is_play:
    print(f"{name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_counter}")
    print(f"## D: {d_counter}")
    print(f"## L: {l_counter}")
    print(f"Win rate: {w_counter / all_counter * 100:.2f}%")
else:
    print(f"{name} hasn't played any games during this season.")
