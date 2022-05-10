rent_hall = float(input())

cake = 0.2 * rent_hall
drinks = cake - cake * 0.45
animator = 1/3 * rent_hall

all_costs = rent_hall + cake + drinks + animator

print(f"{all_costs:.2f}")


