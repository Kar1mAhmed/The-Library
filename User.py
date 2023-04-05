from Book import Book
import random
import datetime


class User:
    curr_id = 0

    def __init__(self, name, age, phone=None):
        self.name = name
        self.age = age
        self.phone = phone
        self.id = User.curr_id
        self.Books = []
        User.curr_id += 1

    def info(self, out=False):
        if out:
            print(f"ID: {self.id}\tUser name : {self.name} User Age : {self.age}\tPhone Number : {self.phone}")
        else:
            return self.name, self.age, self.phone, self.id

    def add_book(self, book_name, author):
        if self._search_book(book_name):
            print("Book is already there")
            return
        new_book = Book(book_name, author, self._generate_date())
        self.Books.append(book_name)

    def _search_book(self, name):
        for book in self.Books:
            if book.name == name:
                return book
        return False

    def read(self, book_name, count):
        book = self._search_book(book_name)
        book.read(count)
