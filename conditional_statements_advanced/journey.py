budget = float(input())
season = input()
destination = ""
type_vacation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
    elif season == "winter":
        budget *= 0.7
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
    elif season == "winter":
        budget *= 0.8
if budget > 1000:
    destination = "Europe"
    budget *= 0.9

if season == "summer":
    type_vacation = "Camp"
    if destination == "Europe":
        type_vacation = "Hotel"
elif season == "winter":
    type_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {budget:.2f}")
