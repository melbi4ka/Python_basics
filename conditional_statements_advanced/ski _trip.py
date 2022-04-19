stay_days = int(input())
room = input()
evaluation = input()
price_room_for_one_person = 18
price_apartment = 25
price_president_apartment = 35
cost = 0

if stay_days < 10:
    if room == "apartment":
        price_apartment *= 0.7
    elif room == "president apartment":
        price_president_apartment *= 0.9

elif 10 <= stay_days <= 15:
    if room == "apartment":
        price_apartment *= 0.65
    elif room == "president apartment":
        price_president_apartment *= 0.85

elif stay_days > 15:
    if room == "apartment":
        price_apartment *= 0.50
    elif room == "president apartment":
        price_president_apartment *= 0.80

if evaluation == "positive":
    if room == "apartment":
        price_apartment *= 1.25
    elif room == "president apartment":
        price_president_apartment *= 1.25
    elif room == "room for one person":
        price_room_for_one_person *= 1.25

if evaluation == "negative":
    if room == "apartment":
        price_apartment *= 0.9
    elif room == "president apartment":
        price_president_apartment *= 0.9
    elif room == "room for one person":
        price_room_for_one_person *= 0.9

if room == "apartment":
    cost = price_apartment * (stay_days-1)
elif room == "president apartment":
    cost = price_president_apartment * (stay_days-1)
elif room == "room for one person":
    cost = price_room_for_one_person * (stay_days - 1)
print(f"{cost:.2f}")









