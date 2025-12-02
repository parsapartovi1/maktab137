# class Library :
#     all_books = []
#
#     def __init__(self, name : str, books : list , members :list):
#         self.name = name
#         self.books = books
#         self.members = members
#
#     def return_books(self , book : Book) :
#         self.book = book
#         # for book3 in self.books :
#         #     all_books.append(book3)
#
#     members = []
#     def add_members(self , member : Member ) :
#
#         for member in self.members :
#             member.mark_as_returned()
#             members.append(member)
#
#     def borrow_book(self , member_id , isban : int ) :
#         # member = self.members[member_id]
#
#
#
#     def return_book(self , member_id , isban : int ) :
#         # member = self.members[member_id]
#
#     def show_all_books(self) :
#         print(all_books)
#
#     def show_all_members(self) :
#         # for member in self.members :
#         #     member.mark_as_returned()
#         #     member.display_info()
#         print(members)

class Member:
    ...

class StudentMember(Member):
    def borrow_book(self, book_title):
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(book_title)
            print(f"{self.name} borrowed '{book_title}'")
        else:
            print("Student access limit reached (3 books)")
        def borrow_book(self, book_title: str):
            super().borrow_book(book_title, max_books=3, duration_days=14)

class TeacherMember(Member):
    def borrow_book(self, book_title):
        if len(self.borrowed_books) < 5:
            self.borrowed_books.append(book_title)
            print(f"{self.name} borrowed '{book_title}'")
        else:
            print("Teacher access limit reached (5 books)")


import pickle
import os

FILE_NAME = "library_data.pkl"
import os

if os.path.exists("library_data.pkl"):
    os.remove("library_data.pkl")
    print("file is removed , another empty library will be created ")

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "rb") as f:
            return pickle.load(f)
    else:
        return {"members": [], "books": []}

def save_data(data):
    with open(FILE_NAME, "wb") as f:
        pickle.dump(data, f)


def search_book_title(data, title):
    for member in data["members"]:
        for book in member.borrowed_books:
            if book.lower() == title.lower():
                print(f"the book '{title}' is taken by {member.name}")
                return

    print(f"the book {title}is available")

def search_member_by_name(data, name):
    for member in data["members"]:
        if member.name.lower() == name.lower():
            member.show_info()
            return
    print(f"only {name} wasn't available")

def report_books(data):
    total_books = len(data["books"])
    borrowed = sum(len(m.borrowed_books) for m in data["members"])
    available = total_books - borrowed
    print(f"\nThe amount of all books is {total_books} ")
    print(f"{borrowed} books is taken")
    print(f"{available} books is available")



data = load_data()
student = StudentMember("Parsa", 1234, "parsa@student.com" , ["extra book"])
teacher = TeacherMember("Sara", 5678, "sara@teacher.com" , ["clean code"])

student.borrow_book("Atomic Habits")
teacher.borrow_book("Clean Code")

data["members"].extend([student, teacher])
data["books"].extend(["Atomic Habits", "Clean Code", "Deep Work", "Sapiens"])

save_data(data)

search_book_title(data, "Atomic Habits")
search_member_by_name(data, "Sara")
report_books(data)

# student = StudentMember("Ali", 1001, "ali@student.com", ["Extra Book"])
# teacher = TeacherMember("Sara", 2001, "sara@teacher.com", ["Clean Code"])
#
# student.borrow_book("Atomic Habits")
# student.borrow_book("Python Basics")
# student.borrow_book("Deep Work")
#
# teacher.borrow_book("Sapiens")
# teacher.borrow_book("1984")
# teacher.borrow_book("Algorithms")
# teacher.borrow_book("Clean Architecture")
# student.show_info()
# teacher.show_info()
member = Member("Parsa Partovi", 1234, "parsa@example.com")
member2 = Member("Parsa Partovi", 1234, "parsa@example.com")
member.borrow_book("Atomic Habits")
member.borrow_book("Deep Work", days_limit=10)
member.show_info()

member.return_books()
member.show_info()