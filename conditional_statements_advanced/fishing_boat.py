budget = int(input())
season = input()
number_fishermen = int(input())
price = 0
discount = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if number_fishermen <= 6:
    discount = 0.9
elif 7 <= number_fishermen <= 11:
    discount = 0.85
elif number_fishermen >= 12:
    discount = 0.75

discounted_price = price * discount
if number_fishermen % 2 == 0 and season != "Autumn":
    discounted_price *= 0.95

rest_money = abs(budget - discounted_price)
if budget >= discounted_price:
    print(f"Yes! You have {rest_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {rest_money:.2f} leva.")
    
