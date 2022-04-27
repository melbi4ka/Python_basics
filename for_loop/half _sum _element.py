import sys

count_num = int(input())
max_num = - sys.maxsize
number_sum = 0
for numbers in range(count_num):
    numeral = int(input())
    if numeral > max_num:
        max_num = numeral
    number_sum += numeral
if max_num == number_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_others = number_sum - max_num
    print(f"Diff = {abs(max_num - sum_others)}")
