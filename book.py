from random import randint

class Book:
    def __init__(self, title, author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'is_available': self.is_available
        }