number = int(input())
current_number = 0
count_one = 0
count_two = 0
count_tree = 0
count_four = 0
count_five = 0

for numbers in range(number):
    current_number = int(input())
    if current_number < 200:
        count_one += 1
    elif current_number <= 399:
        count_two += 1
    elif current_number <= 599:
        count_tree += 1
    elif current_number <= 799:
        count_four += 1
    else:
        count_five += 1
pr_count_one = count_one / number * 100
pr_count_two = count_two / number * 100
pr_count_tree = count_tree/number * 100
pr_count_four = count_four / number * 100
pr_count_five = count_five / number * 100
print(f"{pr_count_one:.02f}%")
print(f"{pr_count_two:.02f}%")
print(f"{pr_count_tree:.02f}%")
print(f"{pr_count_four:.02f}%")
print(f"{pr_count_five:.02f}%")
