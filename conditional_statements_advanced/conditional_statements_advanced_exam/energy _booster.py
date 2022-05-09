fruit = input()
set_dimentions = input()
number_sets = int(input())
price = 0
price_per_set = 0

if set_dimentions == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20
    price_per_set = 2 * price
if set_dimentions == "big":
    if fruit == "Watermelon":
        price = 28.7
    elif fruit == "Mango":
        price = 19.6
    elif fruit == "Pineapple":
        price = 24.8
    elif fruit == "Raspberry":
        price = 15.2
    price_per_set = 5 * price

price_per_all_set = price_per_set * number_sets
if price_per_all_set < 400:
    price_per_all_set *= 1
if 400 <= price_per_all_set <= 1000:
    price_per_all_set *= 0.85
elif price_per_all_set > 1000:
    price_per_all_set *= 0.5

print(f"{price_per_all_set:.2f} lv.")


