import tkinter
from tkinter import END
from book import Book
import booksSDK
tk=tkinter.Tk()
tk.title("Listbox")
listbox=tkinter.Listbox(tk)
#listbox.insert(0,"hello","hi","yo")
#listbox.insert(2,'World')
#listbox.insert(END,'HEY YOU')
#listbox.delete(0)
listbox.pack()
books=[]
def add_object():
    book_title=entry_title.get()
    book_pages=int(entry_pages.get())
    book=Book(book_title,book_pages)
    #WE ARE ADDING THIS BOOK TO OUR DATABASE ALSO
    if booksSDK.add_book(book): #just to confirm that book added,so true and procede further
        listbox.insert(END,book)
        entry_title.delete(0,END)
        entry_pages.delete(0,END)
        books.append(book)
def remove_item():
    book_tuple=listbox.curselection()
    book=books.pop(book_tuple[0])
    if booksSDK.delete_book(book):
        listbox.delete(book_tuple)
for book in booksSDK.get_books():
    listbox.insert(END,book)
    books.append(book)

title=tkinter.Label(tk,text="Book title").pack()
entry_title=tkinter.Entry(tk)
entry_title.pack()
pages=tkinter.Label(tk,text="Book page count")
pages.pack()
entry_pages=tkinter.Entry(tk)
entry_pages.pack()
button=tkinter.Button(tk,text="Add Book",command=add_object)
button.pack()
button=tkinter.Button(tk,text="Remove selected Book",command=remove_item)
button.pack()
tk.mainloop()
