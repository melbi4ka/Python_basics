first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    odd_digit_sum = 0
    even_digit_sum = 0
    number_as_string = str(number)
    for index, digit in enumerate(number_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)
    if odd_digit_sum == even_digit_sum:
        print(number, end=" ")

