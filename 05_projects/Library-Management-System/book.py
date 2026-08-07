class Book:
    
    def __init__(self, book_id, title, author):
        self. id = book_id
        self.title = title 
        self.author = author 
        self.available = True 
        self.borrower = "" 
        self.borrow_count = 0 
        
    def display(self):
        print(f"Book ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {'Yes' if self.available else 'No'}")
        print(f"Borrower: {self.borrower if self.borrower else 'None'}")
        print(f"Borrow Count: {self.borrow_count}")
         
    
    def borrow(self, borrower_name):
        if self.available:
            self.available = False
            self.borrower = borrower_name
            self.borrow_count +=1
            print(f'"{self.title}" has been borrowed by {borrower_name}.')
        else:
            print(f'"{self.title}" is already borrowed by {self.borrower}.')
                        
    def return_book(self):
        if not self.available:
            print(f'"{self.title}" has been returned by {self.borrower}.')
            self.available = True
            self.borrower = ""
        else:
            print(f'"{self.title}" is already in the library.')
            
    
    def to_dict(self):
         return{
             "id": self.id,
             "title": self.title,
             "author": self.author,
             "available": self.available,
             "borrower": self.borrower,
             "borrow_count": self.borrow_count
         }
         
    @classmethod
    def from_dict(cls, data):
        book = cls(
            data['id'],
            data['title'],
            data['author']
        ) 
        book.available = data['available']
        book.borrower = data['borrower']
        book.borrow_count = data['borrow_count']
    
        return book 
    
    def __str__(self):
        return (
            f"Book ID      : {self.id}\n"
            f"Title        : {self.title}\n"
            f"Author       : {self.author}\n"
            f"Available    : {'Yes' if self.available else 'No'}\n"
            f"Borrower     : {self.borrower or 'None'}\n"
            f"Borrow Count : {self.borrow_count}"
        )
 