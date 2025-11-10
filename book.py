import random
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        isbn_num = random.randint(1,10000)
        self.isbn = isbn_num
        self.is_available = True

