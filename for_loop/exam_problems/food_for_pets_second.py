count_days = int(input())
all_quantity = float(input())
biscuits = 0
all_food = 0
sum_cat_food = 0
sum_dog_food = 0
sum_all_biscuits = 0

for numbers in range(1, count_days+1):
    dog_food = int(input())
    cat_food = int(input())
    all_food += cat_food + dog_food
    sum_cat_food += cat_food
    sum_dog_food += dog_food
    if numbers % 3 == 0:
        biscuits = 0.10 * (dog_food + cat_food)
        sum_all_biscuits += biscuits

percent_cat_food = sum_cat_food/all_food * 100
percent_dog_food = sum_dog_food/all_food * 100
percent_all_food = all_food/all_quantity * 100

print(f"Total eaten biscuits: {round(sum_all_biscuits)}gr.")
print(f"{percent_all_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")

