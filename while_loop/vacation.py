excursion_money = float(input())
available_money = float(input())

spending_counter = 0
all_days = 0

while available_money < excursion_money and spending_counter < 5:
    comand = input()
    current_money = float(input())
    all_days += 1
    if comand == "save":
        available_money += current_money
        spending_counter = 0
    elif comand == "spend":
        spending_counter += 1
        available_money -= current_money
        if available_money < 0:
            available_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(f"{all_days}")
if available_money >= excursion_money:
    print(f"You saved the money for {all_days} days.")





