### Practice

#### Exercise 1

class Book:
    
    def __init__(self, title, author, price):
        self.title = title
        self.author= author
        self.price = price
        
    def display(self):
        print("\nBook's Details:")
        print(f"Title: {self.title}")
        print(f"Author:{self.author}")
        print(f"Price: {self.price}")
        
book = Book(
    input("title:"),
    input("author:"),
    float(input("price:"))
)

book.display()


#### Exercise 2

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area_rectangle(self):
        print(f"Area of rectangle: {self.length*self.width}")
        
    def perimeter_rect(self):
        print(f"Perimeter of rectangle: {2*(self.length+self.width)}")
        
rect = Rectangle(
    int(input("length:")),
    int(input("width:"))
)

rect.area_rectangle()
rect.perimeter_rect()


#### Exercise 3

class BankAccount:
    
    def __init__(self, initial_balance= 0.0):
        self.balance = float(initial_balance)
        
    def deposit(self, amount):
        if amount <=0:
            print("Deposit amount must be positive.")
            return
        
        self.balance +=amount
        print(f"Deposited: ${amount:.2f} | New Balance: ${self.balance:.2f}")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("withdrawal amount must be positive.")
            return
        
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f} | New Balance: ${self.balance:.2f}")
    
    def show_balance(self):
        print(f"Current Balance: ${self.balance:.2f}" )

initial = float(input("Initial balance:"))
account = BankAccount(initial)

deposit_amt = float(input("Deposit amount:"))
account.deposit(deposit_amt)

withdraw_amt = float(input("withdrawal amount:"))
account.withdraw(withdraw_amt)

account.show_balance()