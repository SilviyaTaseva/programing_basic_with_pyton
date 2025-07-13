book_name = input()
book_counter = 0
book_found = False

while True:
    current_book = input()
    if current_book == 'No More Books':
        break

    if current_book == book_name:
        book_found = True
        break
    book_counter += 1

if book_found:
    print(f'You checked {book_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {book_counter} books.')