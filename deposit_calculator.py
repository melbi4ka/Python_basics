deposit_sum = float(input())
months_for_deposit = int(input())
interest_rate = float(input())
total_sum = deposit_sum + months_for_deposit*((deposit_sum*interest_rate/100)/12)
print(total_sum)