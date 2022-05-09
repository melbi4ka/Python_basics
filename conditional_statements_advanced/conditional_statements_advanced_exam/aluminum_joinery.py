number_goods = int(input())
type_goods = input()
type_delivery = input()

price = 0


if type_goods == "90X130":
    price = 110
    if 10 < number_goods <= 30:
        price = price
    elif 30 < number_goods <= 60:
        price *= 0.95
    else:
        price *= 0.92
elif type_goods == "100X150":
    price = 140
    if 10 < number_goods <= 40:
        price = price
    elif 40 < number_goods <= 80:
        price *= 0.94
    else:
        price *= 0.90
elif type_goods == "130X180":
    price = 190
    if 10 < number_goods <= 20:
        price = price
    elif 20 < number_goods <= 50:
        price *= 0.93
    else:
        price *= 0.88
elif type_goods == "200X300":
    price = 250
    if 10 < number_goods <= 25:
        price = price
    elif 25 < number_goods <= 50:
        price *= 0.91
    else:
        price *= 0.86

order = price * number_goods
if type_delivery == "With delivery":
    order += 60

if number_goods > 99:
    order *= 0.96

if number_goods < 10:
    print("Invalid order")
else:
    print(f"{order:.2f} BGN")
