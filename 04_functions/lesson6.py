### Calculator with functions

#function created
def add(num1, num2):
        return num1 + num2
def subtract(num1, num2):
        return num1 - num2
def multiply(num1, num2):
        return num1 * num2
def divide(num1, num2):
        return num1 / num2
       
       
#Ask for the input
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

while True:

    #ASk for operation choice
    choice = input("Enter your choice: (+ or - or * or /:)").strip()

    #Function calling
    if choice == "+":
        result = add(num1, num2)

    elif choice == "-":
        result = subtract(num1, num2)

    elif choice == "*":
        result = multiply(num1, num2)

    elif choice == "/":
        if num2 == 0:
            print("Cannot divided by zero.")
        else:
            result = divide(num1, num2)

    else: 
        print("Invalid Choice")
        continue
        

    #Displaying value
    print(f"Result: {result}")
    break