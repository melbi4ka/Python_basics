name_actor = input()
academy_points = float(input())
number_jury = int(input())
lenght_name = 0
actor_points = 0

for numbers in range(number_jury):
    name_jury = input()
    member_points = float(input())
    lenght_name = len(name_jury)
    actor_points = lenght_name * member_points / 2
    academy_points += actor_points
    if academy_points >= 1250.5:
        break

diff = (1250.5 - academy_points)

if academy_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
