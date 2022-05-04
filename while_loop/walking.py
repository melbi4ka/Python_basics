comand = input()
all_steps = 0
is_reached = False

while comand != "Going home":
    current_steps = int(comand)
    all_steps += current_steps
    if all_steps >= 10000:
        is_reached = True
        break
    comand = input()

if comand == "Going home":
    last_steps = int(input())
    all_steps += last_steps
    if all_steps >= 10000:
        is_reached = True

diff = abs(all_steps - 10000)
if is_reached:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")








