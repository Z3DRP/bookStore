import sqlite3

"""
sqlite database
"""


def connect_to_db(db_name='bookdata.db'):
    return sqlite3.connect(db_name)


def create_book_table():
    try:
        # con = sqlite3.connect('bookdata.db')
        # cursor = con.cursor()
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')
        _save_db(con)
    except Exception as e:
        raise Exception(e)


def _save_db(con):
    try:
        con.commit()
        con.close()
    except Exception as e:
        raise Exception(e)


# eventually see if this will work
def _execute(cursor, statement):
    try:
        cursor.execute(statement)
    except Exception as e:
        raise Exception(e)


def add_book(name, author):
    try:
        # con = sqlite3.connect('bookdata.db')
        # cursor = con.cursor()
        con = connect_to_db()
        cursor = con.cursor()
        # this prevent sql injection
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
        _save_db(con)
    except Exception as e:
        raise Exception(e)


def get_all_books():
    try:
        #
        # con = sqlite3.connect('bookdata.db')
        # cursor = con.cursor()
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM books')
# books = cursor.fetchall() # gives list of tuples [(name,author,read), etc]
        # so use list comp to convert list of tuples into dict
        books = [
            {'name': row[0], 'author': row[1], 'read': row[2]}
            for row in cursor.fetchall()
        ]
        con.close()
        return books
    except Exception as e:
        raise Exception(e)


def mark_book_read(name):
    try:
        # con = sqlite3.connect('bookdata.db')
        # cursor = con.cursor()
        con = connect_to_db()
        cursor = con.cursor()
        # prevents sql injection
        cursor.execute('UPDATE books SET read = 1 WHERE name=?', (name, ))
        _save_db(con)
    except ValueError as e:
        raise ValueError(e)


def delete_book(name):
    try:
        # con = sqlite3.connect('bookdata.db')
        # cursor = con.cursor()
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))
        _save_db(con)
    except ValueError as e:
        raise ValueError(e)
