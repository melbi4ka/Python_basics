from math import floor

number_balls = int(input())
all_points = 0
diferent_colour = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0


for numbers in range (number_balls):
    colour = input()
    if colour == "red":
        all_points += 5
        red_balls += 1
    elif colour == "orange":
        all_points += 10
        orange_balls += 1
    elif colour == "yellow":
        all_points += 15
        yellow_balls += 1
    elif colour == "white":
        all_points += 20
        white_balls += 1
    elif colour == "black":
        all_points = floor(all_points / 2)
        black_balls += 1
    else:
        diferent_colour += 1

print(f"Total points: {all_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {diferent_colour}")
print(f"Divides from black balls: {black_balls}")
