class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, file_size, title, author):
        super().__init__(self, title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {super().__str__()}, {self.title} by {self.author}, File Size: {self.file_size}kb"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(self, title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {super().__str__()}, {self.title} by {self.author}, Page count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_books(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)
            






    
