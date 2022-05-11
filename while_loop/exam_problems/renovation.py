from math import ceil

height = int(input())
width = int(input())
not_paint = int(input())

area = height * width * 4
area_for_paint = ceil(area - area * not_paint/100)

comand = input()
while comand != "Tired!":
    paint = int(comand)
    area_for_paint -= paint

    if area_for_paint <= 0:
        break
    comand = input()

if area_for_paint > 0:
    print(f"{ceil(area_for_paint)} quadratic m left.")
elif area_for_paint < 0:
    print(f"All walls are painted and you have {ceil(abs(area_for_paint))} l paint left!")
elif area_for_paint == 0:
    print(f"All walls are painted! Great job, Pesho!")









