# Reverse name

name = "Harina"
print("Reversed:",name[::-1])


#Count Vowels

n=0
vowels = "aeiouAEIOU"
user = input("Enter a sentence:")

for i in user:
    if i in vowels:
        n+=1

print(user)
print("No. of vowels:", n)


#Password Validator

while True:    
    password = input("Enter your password:")

    if len(password) < 8:
        print("Password must be at least 8 character long")        
    else:
        break
            
if "@" in password:
        print("Strong Password")       
else:
    print("Weak Password")
    
    
    
#Mini challenge : Palindrome Checker

word = input("Enter a word:").strip().lower()


if word == word[::-1]:
    print(f"'{word}' is palindrome.")
else: 
    print(f"Entered word '{word}' is not palindrome.")

