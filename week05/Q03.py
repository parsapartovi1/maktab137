class Book :
    total_books = 0
    def __init__(self, title : str, author : str, isban : int ,
                 is_borrowed : bool):
        self.title = title
        self.author = author
        self.isban = isban
        self.is_borrowed = is_borrowed
        Book.total_books += 1


    def mark_as_borrowed (self) :
        self.is_borrowed = True

    def mark_as_returned (self) :
        self.is_borrowed = False

    def display_info(self) :
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isban}")
        print(f"Is Borrowed : {self.is_borrowed}")
        print(f"Total Books: {self.total_books}")

book = Book(title ="atomic habits" , author ="james clear" ,isban = 978_622_6010_22_1,
           is_borrowed=True)
# book2 = Book(title ="think again" , author ="adam grant" ,isban = 978_622_6010_22_3,
#            is_borrowed=False)

book.display_info()