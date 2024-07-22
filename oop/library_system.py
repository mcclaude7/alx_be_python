#class Book:
 #   def __init__(self, title, author):
  #      self.title = title
   #     self.author = author
    
    #def __str__(self):
     #   return f"Book: {self.title} by {self.author}"
    
#class EBook(Book):
 #   def __init__(self, title, author, file_size):
  #      super().__init__(title, author)
   #     self.file_size = file_size

#    def __str__(self):
 #       return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}kb"

#class PrintBook(Book):
 #   def __init__(self, title, author, page_count):
  #      super().__init__(self, title, author)
   #     self.page_count = page_count
    
    #def __str__(self):
     #   return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"

#class Library:
 #   def __init__(self):
  #      self.books = []
    
   # def add_books(self, book):
    #    self.books.append(book)
    
    #def list_books(self):
     #   for book in self.books:
      #      if isinstance(book, EBook):
       #         print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
        #       print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
         #   else:
          #      print(f"Book: {book.title} by {book.author}")
            
# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) :
        return f"{super().__str__()} EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()},PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)






    
