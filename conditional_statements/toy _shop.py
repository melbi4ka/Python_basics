holiday_price = float(input())
number_puzlles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
sum_toys = number_puzlles*2.60 + number_dolls*3 + number_teddy_bears*4.10\
           + number_minions*8.2 + number_trucks*2
number_toys = number_puzlles + number_dolls + number_teddy_bears + number_minions + number_trucks
if number_toys >= 50:
    sum_toys = sum_toys*0.75
rent = sum_toys * 0.1
total_sum = sum_toys - rent
rest_money = abs(total_sum - holiday_price)
if total_sum >= holiday_price:
    print(f"Yes! {rest_money:.2f} lv left.")
else:
    print(f"Not enough money! {rest_money:.2f} lv needed.")

