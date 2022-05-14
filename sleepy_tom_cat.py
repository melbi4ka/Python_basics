holidays = int(input())
holiday_day_minutes = holidays * 127
working_days_minutes = (365 - holidays)*63
play_time = (working_days_minutes + holiday_day_minutes)
time_difference = abs(30000 - play_time)
time_difference_hours = time_difference // 60
time_difference_minutes = time_difference % 60
if play_time < 30000:
    print(f"Tom sleeps well")
    print(f"{time_difference_hours} hours and {time_difference_minutes} minutes less for play")
else:
    print(f"Tom will run away")
    print(f"{time_difference_hours} hours and {time_difference_minutes} minutes more for play")






