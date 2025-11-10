from book import *
from user import *
class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users  = []

    def add_book(self,book):
        self.list_of_books.append(book)
        # print("The book has been borrowed successfully")


    def add_user(self,user):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_isbn):
        for user in self.list_of_users:
            if user.id == user_id:
                for book in self.list_of_books:
                    if book.isbn == book_isbn and book.is_available:
                        user.borrowed_books.append(book)
                        book.is_available = False
                        print("Excellent, the book was borrowed")

    def return_book(self,user_id, book_isbn):
        for user in self.list_of_users:
            if user.user_id == user_id:
                for book in self.list_of_books:
                    if book.book_isbn == book_isbn:
                        user.borrowed_books.pop(book)
                        book.is_available = True

    def list_available_books(self):
        available_books = []
        for book in self.list_of_books:
            if book.is_available:
                available_books.append(book.title)
        return available_books

    def search_book(self,author):
        authors_books = []
        for book in self.list_of_books:
            if book.author == author:
                authors_books.append(book.title)
        return authors_books




book1= Book("hari potter","g.k.roling")
book2= Book("talmud babli","tanaim")
user1 = User("ariel",207827924)
user2 = User("avigail",322869355)
library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_user(user1)
library1.add_user(user2)
library1.borrow_book(207827924,book1.isbn)
library1.borrow_book(207827924,book2.isbn)
print(library1.list_available_books())




















