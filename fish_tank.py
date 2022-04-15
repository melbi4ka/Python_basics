lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())
volume_litters = (lenght * width * height)/1000
needed_litters = volume_litters - (volume_litters*percentage/100)
print(needed_litters)

