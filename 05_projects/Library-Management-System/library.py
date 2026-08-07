import json
from book import Book

class Library:
    def __init__(self):
        self.books = [] 
        self.load_books()
        
    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added successfully.') 
    
    def view_books(self):
        if not self.books:
            print("No books in the libary.")
            return
        
        print("\n---- Library Books ----")
        
        for book in self.books:
            book.display()
            print("-" *30) 
    
    
    def search_book(self, keyword):
        results = []
        
        keyword = str(keyword).lower()
        
        for book in self.books:
            if(
                keyword == str(book.id).lower()
                or keyword in book.title.lower()
                or keyword in book.author.lower()
            ):
                results.append(book)
                
        return results


    def update_book(self, book_id, new_title = None, new_author = None):
        book = self.find_book_by_id(book_id)
        
        if book is None:
            print("Book not found.")
            return      
        if new_title:
            book.title = new_title            
        if new_author:
            book.author = new_author
                    
        print("Book updated successfully.")


    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None


    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        
        if book is None:
            print("Book not found.")
            return
        if not book.available:
            print("Cannot delete a borrowed book.")
            return
        
        self.books.remove(book)
        print(f'"{book.title}" deleted successfully.')


    def borrow_book(self, book_id, borrower_name):
        book = self.find_book_by_id(book_id)
        
        if book is None:
            print("Book not found.")
            return
        book.borrow(borrower_name)
        
        
    def return_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book is None:
            print("Book not found.")
            return
        book.return_book()

    def save_books(self, filename="books.json"):
        try:
            data = [book.to_dict() for book in self.books]

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            print("Books saved successfully.")

        except OSError as e:
            print(f"Error saving books: {e}")
            
                
    def load_books(self, filename="books.json"):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)

                self.books = []

                for item in data:
                    self.books.append(Book.from_dict(item))

                print("Books loaded successfully.")

            except FileNotFoundError:
                print("No previous records found. Starting a new library.")

            except json.JSONDecodeError:
                print("Error: books.json is corrupted.")

    def inventory_report(self):
        total = len(self.books)
        available = sum(1 for book in self.books if book.available)
        borrowed = total - available
        
        print("\n---- Inventory Report ----")
        print(f"Total Books: {total}")
        print(f"Available Books: {available}")
        print(f"Borrowed Books: {borrowed}")

