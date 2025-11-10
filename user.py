from random import randint

class User :
    def __init__(self, name):
        self.name = name
        self.id = randint(1000,9999)
        self.borrowed_books = []


    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'borrowed_books': self.borrowed_books,
        }