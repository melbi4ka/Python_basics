nums = int(input())
current = 1
is_bigger_than_nums = False

for rows in range(1, nums+1):
    for col in range(1, rows + 1):
        if current > nums:
           is_bigger_than_nums = True
           break
        print(current, end=" ")
        current += 1
    if is_bigger_than_nums:
        break
    print()

