class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
class library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books .append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"You have checked out '{title}'") 
                else:
                    print(f"'{title}' is checked out.")
                return
            print(f"'{title}' not found in the library.")


    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"You have returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")



    
