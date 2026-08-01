## Safe Calculator

try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    
    result = num1 / num2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
    
else: 
    print("Result:", result)

finally:
    print("Calculator closed.")