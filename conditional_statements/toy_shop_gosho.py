travel_price = float(input())
numbers_of_puzzles = int(input())
numbers_of_dolls = int(input())
numbers_of_bears = int(input())
numbers_of_minions = int(input())
numbers_of_trucks = int(input())
number_sum = (numbers_of_puzzles * 2.60) + (numbers_of_dolls * 3) + (numbers_of_bears * 4.10) + \
             (numbers_of_minions * 8.20) + (numbers_of_trucks * 2)
number_toys = numbers_of_puzzles + numbers_of_dolls + numbers_of_bears + numbers_of_minions + numbers_of_trucks

if number_toys >= 50:
    number_sum = number_sum * 0.75

rent = number_sum * 0.1
profit = number_sum - rent
needed_sum = abs(profit - travel_price)

if profit >= travel_price:
    print(f'Yes! {needed_sum:.2f} lv left.')
else:
    print(f'Not enough money! {needed_sum:.2f} lv needed.')

