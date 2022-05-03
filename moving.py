width = int(input())
lenght = int(input())
height = int(input())
free_space = width * lenght * height

current_comand = ""
while free_space > 0:
    current_comand = input()
    if current_comand == "Done":
        if free_space > 0:
            print(f"{free_space} Cubic meters left.")
        break
    else:
        comand = int(current_comand)
        free_space -= comand


if free_space < 0:
    needed_space = abs(free_space)
    print(f"No more free space! You need {needed_space} Cubic meters more.")


