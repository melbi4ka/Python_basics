number = int(input())
for numbers in range(1111, 10000):
    numbers_are_special = True
    numbers_as_string = str(numbers)
    for digit in numbers_as_string:
        if int(digit) == 0 or number % int(digit) != 0:
            numbers_are_special = False
            break
    if numbers_are_special:
        print(numbers, end=" ")



