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
        read = input("Did you read this book? (Y/N) : ")

        new_book = do.Book(name, author, read)
        successful_add = database.add_book()
    except ValueError as errMsg:
        print(errMsg)


def list_books():
    list_of_books = database.list_books()
    for book in list_of_books:
        print(book)


def mark_book_read():
    try:
        name = input("Enter name of book to mark as read: ")
        if not isinstance(name, str):
            raise ValueError("Name cannot be numeric")
        else:
            database.mark_book_read(name)
            print(f"{name} has been marked as read")
    except ValueError as errMsg:
        print(errMsg)


def delete_book():
    try:
        name = input("Enter name of book to delete: ")
        if not isinstance(name, str):
            raise ValueError("Name cannot be numeric")
        else:
            database.delete_book(name)
            print(f"{name} has been deleted")
    except ValueError as errMsg:
        print(errMsg)


def menu():
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
        except ValueError as errMsg:
            print(f"Data Error: {errMsg}")
        except Exception as genErrMsg:
            print(f"General Error: {genErrMsg}")


def main():
    print("*** Welcome to the zd3v book archive ***\n")
    menu()


if __name__ == "__main__":
    main()




