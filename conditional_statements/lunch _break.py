from math import ceil
name_serial = input()
movie_time = int(input())
rest_time = int(input())
time_lunch = 1/8 * rest_time
time_break = 1/4 * rest_time
free_time = rest_time - time_lunch - time_break
total_time = abs(free_time - movie_time)
if free_time > movie_time:
    print(f"You have enough time to watch {name_serial} and left with {ceil(total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {ceil(total_time)} more minutes.")
