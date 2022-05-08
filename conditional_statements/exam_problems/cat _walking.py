minutes_per_day = int(input())
number_walkings_per_day = int(input())
cat_calories_per_day = int(input())

all_minutes_walking = minutes_per_day * number_walkings_per_day
all_calories = all_minutes_walking * 5

if all_calories >= 0.5 * cat_calories_per_day:
    print (f"Yes, the walk for your cat is enough. Burned calories per day: {all_calories}.")
else:
    print (f"No, the walk for your cat is not enough. Burned calories per day: {all_calories}.")

