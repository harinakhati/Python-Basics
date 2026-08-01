### Practice

#### Exercise 1
try:
    integer = int(input("Enter an integer:"))
    print(integer)
except ValueError:
    print("Invalid integer.")
    
    
#### Exercise 2

try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    
    division = num1/num2
    print(division)
    
except ValueError:
    print("Invalid value.")

except ZeroDivisionError:
    print("Cannot be divided by zero.")
    
    
#### Exercise 3

filename = input("Enter file name:")

try:
    with open(f"{filename}.txt", "w") as file:
        print(file.write("Hello"))
        
except FileNotFoundError:
    print("File not found.")