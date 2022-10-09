import json
"""
json file storage
format:
[
 {
    'name': 'Design Patterns Explained',
    'author': 'Alan Shalloway',
    'read': True
 }
]
"""

books_file = 'books.json'


def create_book_table():
    # this will initialize the json file with a empty list or will throw error
    # if the json file is empty
    with open(books_file, 'w') as file:
        json.dump([], file)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'].lower() == name.lower():
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    # if list comp does not work with method call then use version below it
    books = [
        book for book in get_all_books()
        if book['name'].lower() != name.lower()
    ]
    # books = get_all_books()
    # books = [book for book in books if book['name'].lower != name.lower()]
    _save_all_books(books)
