from tkinter.messagebox import showinfo
import pickle
import os
from datetime import datetime , timedelta

# class Member :
#     def __init__(self, name : str , member_id :int , email: any ,
#                  borrowed_books : list) :
#
#         self.name = name
#         self.member_id = member_id
#         self.email = email
#         self.borrowed_books = borrowed_books
#
#     def borrowed_books(self) :
#        borrowed = []
#        for book in self.borrowed_books :
#            borrowed.append(book)
#         # print(borrowed)
#     # return self.borrowed_books
#
#     def return_books(self) :
#        for book in self.borrowed_books :
#            self.borrowed_books().remove(book)
#            # print(book)
#
#     def show_info(self) :
#         # print(self.name , self.member_id ,
#         #       self.email , self.borrowed_books)
#         # print(self.borrowed_books)
#         print(f"Name: {self.name}, ID: {self.member_id}, Email: {self.email}")
#         print(f"Borrowed Books: {self.borrowed_books}")
#
# member = Member(name="parsa partovi", member_id=1234, email="ab@gmail.com" , borrowed_books = "atomic habits")
# member.show_info()

from datetime import datetime, timedelta

class Member:
    def __init__(self, name: str, member_id: int, email: str, borrowed_books: list = None):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books else []

    def borrow_book(self, book_title: str, days_limit: int = 14):
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=days_limit)
        self.borrowed_books.append((book_title, borrow_date, due_date))
        print(f"{self.name} borrowed '{book_title}' on {borrow_date.strftime('%Y-%m-%d %H:%M')} (due: {due_date.strftime('%Y-%m-%d %H:%M')})")

    def return_books(self):
        self.borrowed_books.clear()
        print(f"{self.name} has returned all books.")

    def show_info(self):
        print(f"\nName: {self.name} | ID: {self.member_id} | Email: {self.email}")
        print("Borrowed Books:")
        if not self.borrowed_books:
            print("  - None")
        else:
            for book in self.borrowed_books:
                if isinstance(book, tuple) and len(book) == 3:
                    title, borrow_date, due_date = book
                    print(f"  - {title} | Borrowed: {borrow_date.strftime('%Y-%m-%d %H:%M')} | Due: {due_date.strftime('%Y-%m-%d %H:%M')}")
                else:
                    print(f"  - {book} (invalid format)")