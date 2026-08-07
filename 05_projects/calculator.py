
# Define the operation function

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1/num2



#Define menu function

def display_menu():
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    

# Define main function

def main():
    while True:       
        display_menu()
        
        choice = input("Choose an option:")
        
        if choice == "5":
                print("Thank you for using calculator.!")
                break        
            
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Please select 1 to 5.")
            continue
        
        num1, num2 = get_numbers()

        if choice == "1":
            result = add(num1, num2)
            
        elif choice == "2":
            result = subtract(num1, num2)
 
        elif choice == "3":
            result = multiply(num1, num2)
                
        elif choice == "4":
                result = divide(num1, num2)
               
        print(f"Result = {result}\n")


# Define functiont to get numbers

def get_numbers():
    while True:
        try:            
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))            
            return num1, num2
    
        except ValueError:
            print("Invalid input. Please enter numeric value only.")
            
            
## Function call
main()