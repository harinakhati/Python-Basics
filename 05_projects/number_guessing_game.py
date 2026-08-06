import random

#function to generate secret number
def generate_secret_number():
    return random.randint(1, 100)

#guess the number function
def get_guess():
    while True:
        try:            
            guess = int(input("Enter your guess:"))
            
            if 1<= guess <=100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

#define main intuitive
def play_game():
    secret = generate_secret_number()
    attempts = 0
    
    while True:
        guess = get_guess()
        attempts +=1
        
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else: 
            print("Congratulations!\nYou guessed the number.")
            return attempts
            
        
#define main function
def main():
    print("==== Number Guessing Game ====")
    while True:
        attempts = play_game()
        print(f"You guessed the number in {attempts} attempts.")
        
        choice = input("Play again? (Y/N):").strip().upper()
        if choice == "Y":
            continue
        else:
            print("Thanks for playing!")
            break
    

#function calling
main()

