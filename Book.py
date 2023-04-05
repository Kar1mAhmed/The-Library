import random


class Book:
    def __init__(self, name, author, date, pages=None):
        if pages is None:
            pages = random.randint(50, 1000)

        self.name = name
        self.author = author
        self.date = date
        self.pages = pages
        self.books_created = 0
        self.current_page = 0

    def info(self, out=False):
        if out:
            print(f'Book name : {self.name}\t\t Author : {self.author}\t Date : {self.date}')
        return self.name, self.author, self.date

    def read(self, count):
        if self.current_page + count > self.pages:
            pages_left = self.pages - self.current_page
            print(f"You Finished the book, What are you reading man, it was only {pages_left} pages left")
            return
        self.current_page += count
