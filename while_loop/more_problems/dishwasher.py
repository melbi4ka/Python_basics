bottle_detragent = int(input())

counter = 0
plates = 0
pot = 0

quantity_detragent = bottle_detragent * 750

comand = input()
while comand != "End":
    current_command = int(comand)
    counter += 1
    if counter % 3 == 0:
        quantity_detragent -= current_command * 15
        pot += current_command
    else:
        quantity_detragent -= current_command * 5
        plates += current_command
    if quantity_detragent < 0:
        break
    comand = input()

if quantity_detragent >= 0:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pot} pots were washed.")
    print(f"Leftover detergent {quantity_detragent} ml.")
else:
    print(f"Not enough detergent, {abs(quantity_detragent)} ml. more necessary!")
