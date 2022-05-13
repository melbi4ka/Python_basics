price_vegies = float(input())
price_fruits = float(input())
kg_vegies = int(input())
kg_fruits = int(input())
income = (price_vegies * kg_vegies + price_fruits * kg_fruits)/1.94
print(f"{income:.2f}")
