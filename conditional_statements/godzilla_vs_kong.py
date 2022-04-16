film_budget = float(input())
number_supernumerary = int(input())
price_clothes_supernumerary = float(input())
sum_clothes = price_clothes_supernumerary * number_supernumerary
decor = film_budget * 0.1

if number_supernumerary >= 150:
    sum_clothes = sum_clothes * 0.9
total_sum = sum_clothes + decor
rest_money = abs(total_sum - film_budget)
if total_sum > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {rest_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {rest_money:.2f} leva left.")


