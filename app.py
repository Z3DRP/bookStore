from utils import database

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
    books = database.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, read: {read}")


def mark_book_read():
    name = input("Enter the name of the book you just finished reading: ")
    database.mark_book_as_read(name)


def delete_book():
    name = input("enter the name of the book you wish to delete: ")
    database.delete_book(name)


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
                print("Error, unknown operation try again")

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




