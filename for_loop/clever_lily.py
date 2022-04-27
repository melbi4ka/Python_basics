age = int(input())
laundry_price = float(input())
toy_price = int(input())
money = 0
toy = 0
rest_money = 0

for number in range(1, age+1):
    if number % 2 == 0:
        money = money + 10
        rest_money += money - 1
    else:
        toy += 1

total_sum = rest_money + toy * toy_price
dif = abs(total_sum - laundry_price)
if total_sum >= laundry_price:
    print(f"Yes! {dif:.2f}")
else:
    print(f"No! {dif:.2f}")
