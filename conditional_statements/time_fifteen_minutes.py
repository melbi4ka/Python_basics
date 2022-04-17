hour = int(input())
minute = int(input())
hour_in_minutes = hour * 60
time_in_minutes = hour_in_minutes + minute + 15
new_hour = time_in_minutes // 60
new_minutes = time_in_minutes % 60
if new_hour > 23:
    new_hour = 0
if new_minutes < 10:
    print(f"{new_hour}:0{new_minutes}")
else:
    print(f"{new_hour}:{new_minutes}")


