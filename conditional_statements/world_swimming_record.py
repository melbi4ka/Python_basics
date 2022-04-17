record_sec = float(input())
distance_meter = float(input())
sec_per_meter = float(input())
distance_time = distance_meter * sec_per_meter
delay = (distance_meter // 15) * 12.5
total_time = distance_time + delay
lacking_sec = abs(total_time-record_sec)
if total_time < record_sec:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {lacking_sec:.2f} seconds slower.")




