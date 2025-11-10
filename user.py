from random import randint


class User :
    def __init__(self, name):
        self.name = name
        self.id = randint(1000,9999)
        self.borrowed_books = []

