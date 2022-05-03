bad_grades = int(input())
bad_grades_counter = 0
sum_grade = 0
all_task = 0
last_problem = ""
is_ejected = False
task_name = input()

while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades:
            is_ejected = True
            break
    sum_grade += grade
    all_task += 1
    last_problem = task_name
    task_name = input()

if is_ejected:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    average_grade = sum_grade / all_task
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {all_task}")
    print(f"Last problem: {last_problem}")







