from utils import database
from domain_objects import book as do

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Select a option: """


def add_book():
    try:
        name = input("Enter book name: ")
        author = input("Enter author's name: ")
        database.add_book(name, author)
    except ValueError as errMsg:
        print(errMsg)


def list_books():
    try:
        books = database.get_all_books()
        for book in books:
            # python treats 1 and 0 as true and flase
            read = 'Yes' if book['read'] else 'No'
            print(f"{book['name']} by {book['author']}, read: {read}")
    except ValueError as ve:
        print(ve)


def mark_book_read():
    try:
        name = input("Enter the name of the book you just finished reading: ")
        database.mark_book_read(name)
    except ValueError as errMsg:
        print(errMsg)


def delete_book():
    try:
        name = input("Enter the name of the book you wish to delete: ")
        database.delete_book(name)
    except ValueError as errMsg:
        print(errMsg)


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input.lower() != 'q':
        try:
            if user_input == 'a':
                add_book()
            elif user_input == 'l':
                list_books()
            elif user_input == 'r':
                mark_book_read()
            elif user_input == 'd':
                delete_book()
            else:
                print("Error, unknown operation")
            user_input = input(USER_CHOICE)

        except ValueError as errMsg:
            print(f"Data Error: {errMsg}")
        except Exception as genErrMsg:
            print(f"General Error: {genErrMsg}")


def main():
    print("*** Welcome to the zd3v book archive ***\n")
    menu()


if __name__ == "__main__":
    main()




