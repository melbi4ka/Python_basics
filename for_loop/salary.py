open_tabs = int(input())
salary = int(input())
penalty = 0

for numbers in range(open_tabs):
    website = input()
    if website == "Facebook":
        penalty += 150
    elif website == "Instagram":
        penalty += 100
    elif website == "Reddit":
        penalty += 50

rest_salary = salary - penalty

if rest_salary <= 0:
    print(f"You have lost your salary.")
else:
    print(rest_salary)

