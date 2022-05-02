width = int(input())
lenght = int(input())
cake_pieces = width * lenght

current_comand = ""
while cake_pieces > 0:
    current_comand = input()
    if current_comand == "STOP":
        break
    else:
        comand = int(current_comand)
        cake_pieces -= comand


if current_comand == "STOP" and cake_pieces > 0:
    print(f"{cake_pieces} pieces are left.")
else:
    needed_cakes = abs(cake_pieces)
    print(f"No more cake left! You need {needed_cakes} pieces more.")
    
