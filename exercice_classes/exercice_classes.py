from abc import ABC, abstractmethod
from decorateurs import measure_time, instance_counter, log_activity


class Item(ABC):
    def __init__(self,title, author, publication_year):
        self.title, self.author, self.publication_year = title, author, publication_year
    
    def __str__(self):
        return f"{self.title} par {self.author}, {self.publication_year}"
    
    @abstractmethod
    @measure_time
    def is_available(self):
        pass

@instance_counter
class Book(Item):
    def __init__(self, title, author, publication_year,isbn, num_copies):
        super().__init__(title, author, publication_year)
        self.isbn, self.num_copies = isbn, num_copies
        
    def __str__(self):
        return super().__str__() + f"ISBN: {self.isbn}"
    
    @measure_time
    def is_available(self):
        return self.num_copies > 0
    
    def borrow(self):
        self.num_copies -= 1 if self.is_available() else 0
    
    def return_book(self):
        self.num_copies += 1

book = Book("Un titre", "Un auteur", 1234, "345678", 8)
book2 = Book("Un titre", "Un auteur", 1234, "345678", 8)
book.is_available()
str(book)
print(Book.get_instances_count())