class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users  = []

    def add_book(self,book):
        self.list_of_books.append(book)


    def add_user(self,user):
        self.list_of_users.append(user)

    def borrow_book(self,user_id, book_isbn):
        for user in self.list_of_users:
            if user.user_id == user_id:
                for book in self.list_of_books:
                    if book.book_isbn == book_isbn and book.is_available:
                        user.borrowed_books.append(book)
                        book.is_available = False
                    else:
                        return "There is no such book isbn."
            else:
                return "There is no such ID card."


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
                available_books.append(book.name)


    def search_book(self,author):
        authors_books = []
        for book in self.list_of_books:
            if book.author == author:
                authors_books.append(book.name)
        return authors_books




























