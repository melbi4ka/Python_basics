from math import floor
from math import ceil
square_m_vineyard = int(input())
grape_square_m = float(input())
needed_liters_wine = int(input())
number_workers = int(input())
all_grape = square_m_vineyard * grape_square_m
vine_grape = all_grape * 0.4
grape_per_litter = vine_grape /2.5
rest_wine = abs(grape_per_litter - needed_liters_wine)
rest_wine_per_workers = rest_wine / number_workers
if grape_per_litter >= needed_liters_wine:
    print(f"Good harvest this year! Total wine: {floor(grape_per_litter)} liters.")
    print(f"{ceil(rest_wine)} liters left -> {ceil(rest_wine_per_workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(rest_wine)} liters wine needed.")
