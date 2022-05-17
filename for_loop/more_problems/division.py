num = int(input())
group_two = 0
group_three = 0
group_four = 0

for n in range(num):
    current_num = int(input())

    if current_num % 2 == 0:
        group_two += 1
    if current_num % 3 == 0:
        group_three += 1
    if current_num % 4 == 0:
        group_four +=1


two_percent = group_two / num * 100
three_percent = group_three / num * 100
four_percent = group_four / num * 100

print(f"{two_percent:.2f}%")
print(f"{three_percent:.2f}%")
print(f"{four_percent:.2f}%")

