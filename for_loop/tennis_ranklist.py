from math import floor

numbers_tournaments = int(input())
initial_points = int(input())
tournament_points = 0
win_tournaments = 0

for numbers in range (numbers_tournaments):
    stage_tournament = input()
    if stage_tournament == "W":
        tournament_points += 2000
        win_tournaments += 1
    elif stage_tournament == "F":
        tournament_points += 1200
    elif stage_tournament == "SF":
        tournament_points += 720

all_points = tournament_points + initial_points
average_point = tournament_points / numbers_tournaments
percent_win = win_tournaments / numbers_tournaments * 100

print(f"Final points: {all_points}")
print(f"Average points: {floor(average_point)}")
print(f"{percent_win:.2f}%")


