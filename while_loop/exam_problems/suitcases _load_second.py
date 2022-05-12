capacity = float(input())
bag_counter = 0
comand = input()

while comand != "End":
    suitcase = float(comand)
    if (bag_counter+1) % 3 == 0:
        suitcase *= 1.1

    if capacity >= suitcase:
        capacity -= suitcase
    else:
        print("No more space!")
        break
    bag_counter += 1
    comand = input()

if comand == "End":
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {bag_counter} suitcases loaded.")
