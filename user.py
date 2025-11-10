from book import *
class User :
    def __init__(self, name, id,):
        self.name = name
        self.id = id
        self.borrowed_books = []



    def borrowed_books1(self):
        for book in self.borrowed_books:
            print(book.title)


