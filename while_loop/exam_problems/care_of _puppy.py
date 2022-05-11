purchased_food = int(input())
purchased_food_grams = purchased_food * 1000
eaten_food = 0


comand = input()
while comand != "Adopted":
    current_command = int(comand)
    eaten_food += current_command
    comand = input()

diff = abs(eaten_food - purchased_food_grams)
if eaten_food > purchased_food_grams:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")



