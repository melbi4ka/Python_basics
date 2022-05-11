import sys

number_films = int(input())
max_rating = - sys.maxsize
min_rating = sys.maxsize
average_rating = 0
max_film = ""
min_fim = ""

for numbers in range(number_films):
    film_name = input()
    film_rating = float(input())
    if film_rating >= max_rating:
        max_rating = film_rating
        max_film = film_name
    if film_rating <= min_rating:
        min_rating = film_rating
        min_film = film_name
    average_rating += film_rating
print (f"{max_film} is with highest rating: {max_rating:.1f}")
print(f"{min_film} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating/number_films:.1f}")


