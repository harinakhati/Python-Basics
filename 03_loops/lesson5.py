## Print Numbers

for i in range(1,11):
    print(i)
    
    
##Even numbers

for i in range(21,2,-1):
    print(i/2)
    
## Countdown

for i in range(11,0,-1):
    print(i)
    
    
## Sum of numbers

n = int(input("Enter a number:"))
total = 0

for  i in range(n):
    total +=i
print(total)



#Guess secret number

# simple one
num = 7

while True:
    user = int(input("Enter a number:"))
    
    if user == num:
            print("Congratulations! You guessed correctly.")
            break

    print("Wrong! Try again.")
    
    
## using try and except
secret = 7
attempts = 0
while True:
    user = input("Guess the number (or 'q' to quit): ")
    if user.lower() == 'q':
        print("Quit — better luck next time.")
        break
    try:
        guess = int(user)
    except ValueError:
        print("Please enter a valid integer.")
        continue
    attempts += 1
    if guess == secret:
        print(f"Congratulations! You guessed correctly in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")