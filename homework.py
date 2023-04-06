# pylint: disable= missing-docstring
from typing import List

class Book:
    def __init__(self, book_name: str, book_qty: int, book_id: int) -> None:
        self.book_name = book_name
        self.book_qty = book_qty
        self.book_id = book_id
        self.state = False
    
    def set_book_state(self):
        self.state = True
    
    def get_book_state(self) -> bool:
        return self.state

class Users:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.take_books = []

class System:
    book_list = []
    _users_db = []
    
    @classmethod
    def add_books(cls, collection: Book) -> None:
        cls.book_list.append(collection)
    
    @classmethod
    def add_user(cls, user_data: Users) -> None:
        cls._users_db.append(user_data)

    @classmethod
    def borrow_book(cls, user: Users, book_id: int) -> None:
        for book in cls.book_list:
            if book.book_id == book_id:
                if book.book_qty > 0:
                    book.book_qty -= 1
                    user.take_books.append(book)
                    print(f"{user.name} take {book.book_name}. Left: {book.book_qty}")
                    return
                else:
                    print("nebera")
            print("blogas id")

    @classmethod
    def return_book(cls, user: Users, book_id: int) -> None:
        for book in cls.book_list:
            if book.book_id == book_id:
                book.book_qty += 1
                user.take_books.remove(book)
                print(f"{user.name} return {book.book_name}. Qty: {book.book_qty}")
                return
            print("blogas id")



book1 = Book(book_name= "Kur gieda veziai", book_qty=5, book_id=1111)
book2 = Book(book_name= "Kur gieda eziai", book_qty=5, book_id=1112)
book4 = Book(book_name= "Kur gieda bebrai", book_qty=5, book_id=1113)
System.add_books(book1)
System.add_books(book2)
System.add_books(book4)
user1 = Users(name= "Linas", surname= "Stonkus")
System.add_user(user_data= user1)
System.borrow_book(user= user1, book_id=1111)
System.return_book(user= user1, book_id=1111)

