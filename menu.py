from library import Library
from library import Book
from library import User


def menu():
    option = 0
    while option != '7':
        option = input(
            'pick an option\n1. Add Book\n2. Add User\n3. Borrow Book\n4. return a book\n5.see all available books\n6. search a book\n7. Save & Exit\n\n  ')
        if option == '1':
            title = input('please enter the title of the book: ')
            author = input('please enter the author of the book: ')
            book = Book(title,author)
            Library.add_book(book)
            print(book.title)
        elif option == '2':
            name = input('what is your name? ')
            user = User(name)
            Library.add_user(user)
        elif option == '3':
            user = input('what is your name? ')
            book = input('what book do you want to take?')
            Library.borrow_book(user,book)
            print('done')
        elif option == '4':
            print('book returned')
        elif option == '5':
            Library.list_available_books()
        elif option == '6':
            print('search book')
        elif option == '7':
            print('exiting...')
            break
        else:
            print('invalid choice, try again')


print()
menu()
