type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0
sum_flowers = 0

if type_flowers == "Roses":
    price = 5
    sum_flowers = number_flowers * price
    if number_flowers > 80:
        sum_flowers *= 0.90
elif type_flowers == "Dahlias":
    price = 3.8
    sum_flowers = number_flowers * price
    if number_flowers > 90:
        sum_flowers *= 0.85
elif type_flowers == "Tulips":
    price = 2.8
    sum_flowers = number_flowers * price
    if number_flowers > 80:
        sum_flowers *= 0.85
elif type_flowers == "Narcissus":
    price = 3
    sum_flowers = number_flowers * price
    if number_flowers < 120:
        sum_flowers *= 1.15
elif type_flowers == "Gladiolus":
    price = 2.5
    sum_flowers = number_flowers * price
    if number_flowers < 80:
        sum_flowers *= 1.20

needed_sum = abs(budget - sum_flowers)

if budget >= sum_flowers:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {needed_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {needed_sum:.2f} leva more.")






