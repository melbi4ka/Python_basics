kilometers = int(input())
type_travel = input()
travel_sum = 0
if type_travel == "day":
    if kilometers < 20:
        travel_sum = 0.70 + kilometers * 0.79
    elif 20 <= kilometers < 100:
        travel_sum = kilometers * 0.09
    else:
        travel_sum = kilometers * 0.06
if type_travel == "night":
    if kilometers < 20:
        travel_sum = 0.70 + kilometers * 0.9
    elif 20 <= kilometers < 100:
        travel_sum = kilometers * 0.09
    else:
        travel_sum = kilometers * 0.06
print(f"{travel_sum:.2f}")








