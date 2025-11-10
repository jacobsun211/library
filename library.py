import json
from library.book import Book
from library.user import User

class Library:
    with open('books.json','w')as f:
        json.dump([],f)
    with open('users.json','w')as f:
        json.dump([],f)

    @staticmethod
    def add_book(book):
        with open('books.json', 'r')as f:
            books = json.load(f)
        books.append(book.to_dict())
        with open('books.json', 'w')as f:
            json.dump(books,f)

    @staticmethod
    def add_user(user):
        with open('users.json', 'r')as f:
            users = json.load(f)
        users.append(user)
        with open('users.json', 'w') as f:
            json.dump(users,f)

    @staticmethod
    def borrow_book(user_id, book_isbn):
        with open("users.json",'r')as f:
            users = json.load(f)
        for user in users:
            if user.id == user_id:
                with open('books.json','r') as f:
                    books = json.load(f)
                for book in books:
                    if book.isbn == book_isbn and book.is_available:
                        user.borrowed_books.append(book)
                        book.is_available = False
                        print(f'{book} is borrowed')

    @staticmethod
    def return_book(user_id, book_isbn):
        with open('users.json','r')as f:
            users = json.load(f)
        for user in users:
            if user.id == user_id:
                with open('books.json','r') as f:
                    books = json.load(f)
                for book in books:
                    if book.isbn == book_isbn:
                        user.borrowed_books.pop(book)
                        book.is_available = True

    @staticmethod
    def list_available_books():
        with open('books.json', 'r') as f:
            books = json.load(f)
        for book in books:
            print(f'title: {book['title']}; author: {book['author']}; isbn: {book['isbn']}')

    @staticmethod
    def search_book(author):
        authors_books = []
        with open('books.json', 'r') as f:
            books = json.load(f)
        for book in books:
            if book.author == author:
                authors_books.append(book.name)
        return authors_books


book = Book('harry potter', "JK rowling")
Library.add_book(book)
user = User('jacob')
Library.borrow_book(user.id,book.isbn)
Library.list_available_books()


