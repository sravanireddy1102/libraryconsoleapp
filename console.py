import booksSDK
from book import Book
def print_menu():
    print("""Choose an option:
    1.print all books
    2.add a book
    3.update a book
    4.delete a book
    """)
while True:
    print_menu()
    response=int(input())
    if response==1:
        for book in booksSDK.get_books():
            print(book)
    elif response==2:
        print("What is the name of the book")
        title=input()
        print("How many pages is the book?")
        pages=int(input())
        book=Book(title,pages)
        print(booksSDK.add_book(book))
    elif response==3:
        print("updating a book")
        print("What is the current title?")
        current_title=input()
        print("Number of pages in the book?")
        current_pages=int(input())
        book=Book(current_title,current_pages)
        new_title=input("New title please")
        new_pages=input("No of pages ")
        print(booksSDK.update_book(book,new_title,new_pages))
    elif response==4:
        title_book=input("Enter the title of the book ")
        pages=int(input("Number of pages in the book"))
        book=Book(title_book,pages)
        booksSDK.delete_book(book)
    else:
        print("Thank you for using our app")
        break
