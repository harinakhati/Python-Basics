from book import Book
from library import Library

def main():
    library = Library()
    
    while True:
        print("\n---------- Library Management -----------")
        print("1. View Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Inventory Report")
        print("9. Save Books")
        print("10. Exit")
        print("----------------------------------------")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            library.view_books()
        elif choice == "2":
            try:
                book_id = int(input("Book ID: "))
            except ValueError:
                print("Invalid Book ID.")
                continue

            title = input("Title: ")
            author = input("Author: ")

            if library.find_book_by_id(book_id):
                print("Book ID already exists.")
                continue

            library.add_book(Book(book_id, title, author))
        elif choice == "3":
            keyword = input("Search:")
            results = library.search_book(keyword)
            
            if results:
                for book in results:
                    book.display()
                    print("-"*30)
            else:
                print("No matching books found.")
        elif choice == "4":
            try:
                book_id = int(input("Book ID:"))
            except ValueError:
                print("Invalid Book ID.")
                continue
            
            new_title = input("New Title (leave blank to keep):")
            new_author = input("New Author (leave blank to keep):")
            
            library.update_book(
                book_id, 
                new_title if new_title else None, 
                new_author if new_author else None
                )
        elif choice == "5":
            try:
                book_id = int(input("Book ID:"))
            except ValueError:
                print("Invalid Book ID.")
                continue
            library.delete_book(book_id) 
        elif choice == "6":
            try:
                book_id = int(input("Book ID:"))
            except ValueError:
                print("Invalid Book ID.")
                continue         
            borrower = input("Borrower's Name:")
            library.borrow_book(book_id, borrower)
        elif choice == "7":
            try:
                book_id = int(input("Book ID:"))
            except ValueError:
                print("Invalid Book ID.")
                continue
            library.return_book(book_id) 
        elif choice == "8":
            library.inventory_report()     
        elif choice == "9":
            library.save_books() 
        elif choice == "10":
            answer = input("Save before exiting? (Y/N):").strip().lower()
            
            if answer == "y":
                library.save_books()
                
            print("Thank you for using the Library Management System.")
            break  
        else:
            print("Invalid choice. Please try again.")
   
        
if __name__ == "__main__":
    main()       
    