x = float(input())
y = float(input())
h = float(input())
front_back_walls = (x**2-1.2*2) + x**2
# print(front_back_walls)
side_walls = (x*y-1.5**2)*2
#print(side_walls)
roof = x*y*2 + (x*h/2)*2
#print(roof)
green_paint = (front_back_walls + side_walls)/3.4
red_paint = roof / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")


