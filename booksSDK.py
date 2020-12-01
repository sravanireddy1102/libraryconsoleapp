import sqlite3
from book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()
c=cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT,pages INTEGER)')
c.connection.close()
def add_book(book):
    c=cursor()
    #Lets say after adding a book to the table we wanna return id 
    with c.connection:
        c.execute('INSERT INTO books VALUES (?,?)',(book.title,book.pages))
    c.connection.close()
    return c.lastrowid
   
def get_books():
    c=cursor()
    books_objects=[]
    with c.connection:
       for book in c.execute('SELECT * FROM books'):
            books_objects.append(Book(book[0],book[1]))
    c.connection.close()
    return books_objects
def get_book_by_title(title):
    c=cursor()
    with c.connection: #automatically commits the code but doesnt close automatically
        c.execute('SELECT * FROM books WHERE title=?',(title,))
        data=c.fetchone()
    c.connection.close()
    if not data:
        return None
    return Book(data[0],data[1])
def update_book(book,new_title,new_pages):
    c=cursor()
    with c.connection:
        c.execute("UPDATE books SET title=?,pages=? WHERE title=? AND pages=? ",(new_title,new_pages,book.title,book.pages))
    book=get_book_by_title(new_title)
    c.connection.close()
    return book
def delete_book(book):
    c=cursor()
    with c.connection:
        c.execute("DELETE FROM books WHERE title=? AND pages=?",(book.title,book.pages))
    c.connection.close()
