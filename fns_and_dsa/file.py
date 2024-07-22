class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is being created.")

    def __del__(self):
        print(f"Person object for {self.name} is being deleted. Farewell, {self.name}!")

person1 = Person("claude", 12)
del person1

class Book:
    def __init__(self, title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    def __repr__(self):
        return f"Title: {self.title} Author: {self.author} Pages: {self.pages}"
    
books = Book("Tintin au congo","Helge", 50)
print(str(books))
print(repr(books))


    





