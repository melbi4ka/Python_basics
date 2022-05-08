juri_nums = int(input())
command = input()
counter = 0
sum_average_grade = 0
while command != "Finish":
    counter += 1
    sum_grade = 0
    for numbers in range(juri_nums):
        grade = float(input())
        sum_grade += grade
        average_grade = sum_grade / juri_nums
    print(f"{command} - {average_grade:.2f}.")
    sum_average_grade += average_grade
    command = input()
print(f"Student's final assessment is {sum_average_grade/counter:.2f}.")







