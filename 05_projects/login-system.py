## Login System

password = input("Enter your password:")

attempts = 3

while attempts>0:
    entered = input("Enter password:")
    
    if entered == password:
        print("Login successful.")
        break
    
    attempts -= 1
    print(f"Incorrect password. Attempts left: {attempts}")
    
else:
    print("Account locked.")
    
