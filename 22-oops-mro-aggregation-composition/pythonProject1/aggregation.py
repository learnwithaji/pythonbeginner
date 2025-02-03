class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

book1 = Book("Python Basics")
book2 = Book("Advanced Python")

library = Library("City Library")
library.add_book(book1)
library.add_book(book2)


