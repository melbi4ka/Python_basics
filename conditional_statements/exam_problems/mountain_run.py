from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_climbing_for_one_meter = float(input())

all_time_climbing = distance_in_meters * time_climbing_for_one_meter
delay = floor(distance_in_meters / 50) * 30
total_time = all_time_climbing + delay

if total_time >= record_in_seconds:
    diff = abs(record_in_seconds - total_time)
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")

