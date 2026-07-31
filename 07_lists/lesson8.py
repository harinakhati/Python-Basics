#Practice 

### 1
numbers = []

for i in range(0,5):
    number = int(input(f"Enter {i+1} numbers:"))

    numbers.append(number)
    
print("Entered numbers:", numbers)
print(f"The largest number: {max(numbers)}")
print(f"The smallest number: {min(numbers)}")
print(f"The sum of numbers: {sum(numbers)}")


### 2

word = input("Enter a word:")
letters = []

for i in range(len(word)):
    letters.append(word[i])
    
print(letters)
    
    
    
### 3 - a shopping cart program

items = []

#Function defining

def add_item():
    item = input("Enter items:").strip()
    items.append(item)
    print("Item Added.")

def view_item():
    if len(items) == 0:
        print("Your cart is empty.")
    else:
        print("Your Items:")
        for i in range(len(items)):
            print(f" {i+1}.{items[i]}") 

def remove_item():
    if len(items) == 0:
                print("Your cart is empty.")
    else:
        for i in range(len(items)):
            print(f"{i+1}.{items[i]}")
            
        index = int(input("Enter item number:"))-1
        
        if 0 <= index < len(items):
            removed = items.pop(index)
            print(f"Removed Items: {removed}")
        else:
            print("Invalid item number.")
                        
def exit():
    print("Happy Shopping!")


while True:
    print("Shopping Cart Menu:\n")
    print("\n1. Add items")
    print("2. View items")
    print("3. Remove items")
    print("4. Exit")
       
    choice = input("Choose an option:").strip()
    
    if choice == "1":
        add_item()
        
    elif choice == "2":
        view_item()
                
    elif choice == "3":
        remove_item()
                
    elif choice == "4":
        exit()
        break

    else:
        print("Invalid Choice.Please choose valid one!")

