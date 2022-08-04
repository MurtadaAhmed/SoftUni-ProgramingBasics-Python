faviorit_book = input()
book_count = 0
book_is_found = False
book_name = input()
while book_name != "No More Books":
    if book_name == faviorit_book:
        book_is_found = True
        break
    else:
        book_name = input()
        book_count += 1

if book_is_found:
    print(f"You checked {book_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")