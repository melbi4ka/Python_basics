time_first = int(input())
time_second = int(input())
time_third = int(input())
total_sum = time_first + time_second + time_third
minutes = total_sum // 60
seconds = total_sum % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
