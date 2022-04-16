from math import floor
book_pages = int(input())
pages_per_hour = int(input())
days = int(input())
day_pages = book_pages / pages_per_hour
needed_hours = day_pages / days
print(floor(needed_hours))

