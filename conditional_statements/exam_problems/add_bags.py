bags_over_twenty = float(input())
kg_bags = float(input())
days_to_trip = int(input())
number_bags = int(input())

price = 0
if kg_bags < 10:
    price = 0.2 * bags_over_twenty
elif kg_bags <= 20:
    price = 0.5 * bags_over_twenty
else:
    price = bags_over_twenty

if days_to_trip < 7:
    price *= 1.4
elif days_to_trip <= 30:
    price *= 1.15
else:
    price *= 1.1

all_price = number_bags * price
print(f"The total price of bags is: {all_price:.2f} lv.")
