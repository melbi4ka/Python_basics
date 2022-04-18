month = input()
number_nights = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_apartment = 65
    price_studio = 50
    if 7 < number_nights < 14 and (month == "May" or month == "October"):
        price_studio *= 0.95
    if number_nights > 14 and (month == "May" or month == "October"):
        price_studio *= 0.70

elif month == "June" or month == "September":
    price_apartment = 68.70
    price_studio = 75.20
    if number_nights > 14 and (month == "June" or month == "September"):
        price_studio *= 0.80

elif month == "July" or month == "August":
    price_apartment = 77
    price_studio = 76

if number_nights > 14:
    price_apartment *= 0.9

all_price_apartment = price_apartment * number_nights
all_price_studio = price_studio * number_nights

print(f"Apartment: {all_price_apartment:.2f} lv.")
print(f"Studio: {all_price_studio:.2f} lv.")


