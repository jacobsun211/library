from library import  *

def menu():
    option = input('pick an option\n1. Add Book\n2. Add User\n3. Borrow Book\n4. return a book\n5.see all available books\n6. search a book\n7. Save & Exit')
    while option != '7':
        if option == '1':
            print('book added!')
        elif option == '2':
            print('user added!')
        elif option == '3':
            print('book borrowed!')
        elif option == '4':
            print('book returned')
        elif option == '5':
            print('list of all books')
        elif option == '6':
            print('search book')

        elif option == '7':
            print('exiting...')
            break
        else:
            print('invalid choice, try again')


