from multipledispatch import dispatch
from domain_objects import book as do

"""in memoory list db for now"""
books = []


@staticmethod
@dispatch(str, str)
def add_book(name, author):
    original_len = len(books)
    try:
        new_book = do.Book(name, author)
        # books.append({'name': name, 'author': author, 'read': False})
        books.append(new_book)
    except ValueError:
        raise ValueError("A error occurred while inserting book")
    if len(books) > original_len:
        return True
    else:
        return False


@staticmethod
@dispatch(do.Book)
def add_book(new_book):
    original_len = len(books)
    try:
        books.append(new_book)
    except ValueError:
        raise ValueError("A error occurred while inserting book")
    if len(books) > original_len:
        return True
    else:
        return False


@staticmethod
def list_books():
    return books


@staticmethod
def mark_book_read(name):
    try:
        for book in books:
            if book['name'] == name:
                book['read'] = True
    except ValueError:
        raise ValueError("Error, book not found")


@staticmethod
def delete_book(name):
    try:
        for old_book in books:
            if old_book['name'] == name:
                books.remove(old_book)
    except ValueError:
        raise ValueError("Error, book was not found")
