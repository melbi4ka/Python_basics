favorite_book = input()
book_counter = 0
is_found = False
book = input()

while book != "No More Books":
    if book == favorite_book:
        is_found = True
        break
    book_counter += 1
    book = input()


if is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")


