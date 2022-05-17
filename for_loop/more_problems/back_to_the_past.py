legacy_money = float(input())
year_in_past = int(input())
year_counter = 17

for years in range(1800, year_in_past + 1):
    year_counter += 1

    if years % 2 == 0:
        legacy_money -= 12000
    if years % 2 == 1:
        legacy_money -= 12000 + (50 * year_counter)

if legacy_money >= 0:
    print(f"Yes! He will live a carefree life and will have {legacy_money:.2f} dollars left.")
else:
    print(f"He will need {abs(legacy_money):.2f} dollars to survive.")
    
