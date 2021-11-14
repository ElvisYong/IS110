book_author_dict = {"Harry Potter and the Sorcerer's Stone": 'J.K. Rowling',
                    "Turtles All the Way Down": 'John Green',
                    "Animal Farm and 1984": 'George Orwell',
                    "The Da Vinci Code": 'Dan Brown',
                    "Harry Potter and the Goblet of Fire": 'J.K. Rowling',
                    "Origin": 'Dan Brown'}

search = input('Do you want to search for the authoer of a book? [Y|N] ')
while search == 'Y':
    title = input('Please enter a book title: ')
    if title in book_author_dict:
        print(f'The author of the book is {book_author_dict[title]}')
    else:
        print('Book not found.')
    search = input('Do you want to continue? [Y|N]')
