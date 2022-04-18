exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
difference = exam_time - arrival_time

if difference < 0:
    print("Late")
    difference = abs(difference)
    if arrival_time != exam_time:
        hours = difference // 60
        minutes = difference % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{minutes} minutes after the start")

elif 0 <= difference <= 30:
    print("On time")
    if arrival_time != exam_time:
        hours = difference // 60
        minutes = difference % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours efore the start")
        else:
            print(f"{minutes} minutes before the start")
else:
    print("Early")
    if arrival_time != exam_time:
        hours = difference // 60
        minutes = difference % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{minutes} minutes before the start")








