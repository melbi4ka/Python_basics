price_kilo_mackerel = float(input())
price_kilo_sprat = float(input())
kg_bonito_horse = float(input())
kg_horse_mackerel = float(input())
kg_shell = int(input())
sum_bonito_horse = price_kilo_mackerel*1.6*kg_bonito_horse
sum_horse_mackerel = price_kilo_sprat*1.8*kg_horse_mackerel
sum_shell = kg_shell * 7.5
all_costs = sum_bonito_horse + sum_horse_mackerel + sum_shell
print(f"{all_costs:.2f}")
