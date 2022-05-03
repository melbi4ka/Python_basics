rest_sum = float(input())
rest_sum = int(rest_sum * 100)
coins_counter = 0

while rest_sum != 0:
    if rest_sum // 200 > 0:
        coins_counter += rest_sum // 200
        rest_sum = rest_sum % 200
    elif rest_sum // 100 > 0:
        coins_counter += rest_sum // 100
        rest_sum = rest_sum % 100
    elif rest_sum // 50 > 0:
        coins_counter += rest_sum // 50
        rest_sum = rest_sum % 50
    elif rest_sum // 20 > 0:
        coins_counter += rest_sum // 20
        rest_sum = rest_sum % 20
    elif rest_sum // 10 > 0:
        coins_counter += rest_sum // 10
        rest_sum = rest_sum % 10
    elif rest_sum // 5 > 0:
        coins_counter += rest_sum // 5
        rest_sum = rest_sum % 5
    elif rest_sum // 2 > 0:
        coins_counter += rest_sum // 2
        rest_sum = rest_sum % 2
    elif rest_sum // 1 > 0:
        coins_counter += rest_sum // 1
        rest_sum = rest_sum % 1

print(coins_counter)




