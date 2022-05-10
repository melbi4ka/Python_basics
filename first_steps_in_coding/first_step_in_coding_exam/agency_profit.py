name_avio = input()
old_ticket = int(input())
child_ticket = int(input())
price_per_old = float(input())
tax_flight = float(input())

price_per_child = price_per_old * 0.3 + tax_flight
price_per_old += tax_flight

agency_profit = (old_ticket * price_per_old + child_ticket * price_per_child) * 0.2

print(f"The profit of your agency from {name_avio} tickets is {agency_profit:.2f} lv.")
