from User import User
from Book import Book
from Helper import *


# Singleton Class
class Library:
    user_count = 0
    book_count = 0

    def __init__(self):
        self.Users = []
        self.Books = []

        ### USERS CONTROL ###

    def add_user(self, name=None, age=None, phone=None):
        if name is None:
            name = generate_name()
        if age is None:
            age = generate_age()
        if phone is None:
            phone = generate_phone_number()

        new_user = User(name, age, phone)
        self.Users.append(new_user)
        Library.user_count += 1

    def remove_user(self, user_id):
        for user in self.Users:
            if user.id == user_id:
                self.Users.remove(user)
                Library.user_count -= 1
                print("User deleted Successfully")
                return
        print("User not found")

    def search_user(self, search_query):
        res = []
        for user in self.Users:
            if search_query == user.name or \
                    search_query == str(user.id) or \
                    search_query == user.phone:
                res.append(user)
        print("Search Result")
        if len(res) == 0:
            print("No match")
        else:
            for user in res:
                user.info(out=True)

    def show_users(self):
        for user in self.Users:
            user.info(out=True)

    def get_random_user_name(self):
        idx = random.randint(0, len(self.Users) - 1)
        return self.Users[idx].name

        ### BOOKS CONTROL ###

    def add_book(self, book_name, author=None, date=None):
        if self._book_exist(book_name):
            print("Book is already exist")
            return

        if author is None:
            author = generate_name()
        if date is None:
            date = generate_date()

        new_book = Book(book_name, author, date)
        self.Books.append(new_book)
        Library.book_count += 1

    def remove_book(self, book_name):
        for book in self.Books:
            if book.name == book_name:
                self.Books.remove(book)
                print("Book Removed")
                self.book_count -= 1
                return
        print("Book Not Found")

    def search_book(self, search_query):
        res = []
        for book in self.Books:
            if search_query == book.name or \
                    search_query == book.author or \
                    search_query == book.date:
                res.append(book)
        print("Search Result")
        if len(res) == 0:
            print("No match")
        else:
            for book in res:
                book.info(out=True)

    def show_books(self):
        for book in self.Books:
            book.info(out=True)

    def _book_exist(self, book_name):
        for book in self.Books:
            if book.name == book_name:
                return True
        return False


if __name__ == "__main__":
    lib = Library()

    lib.add_book("How to Have Friends")
    lib.add_book("How to Fuck Girls")

    lib.search_book('22')
    lib.search_book("How to Have Friends")

    # lib.add_user()
    # lib.add_user()
    #
    # lib.show_users()
    #
    # print('*' * 50)
    # print(lib.user_count)
    # lib.remove_user(2)
    # print('*' * 50)
    #
    # lib.show_users()
    # print(lib.user_count)
    #
    # print('-' * 100)
    # lib.add_book("Inside Us")
    # lib.add_book("Outside the world")
    # lib.add_book("This IS THE TRUTH")
    # lib.add_book("HELLO WORLD IN 100 PROGRAMING LANGUAGE")
    #
    # lib.show_books()
    # print(f"Current book count : {lib.book_count}")
    # print('*' * 50)
    #
    # lib.remove_book("HELLO WORLD IN 100 PROGRAMING LANGUAGE")
    #
    # lib.show_books()
    # print(f"Current book count : {lib.book_count}")
