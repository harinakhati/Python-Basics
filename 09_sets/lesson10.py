### Practice

#### Exercise 1


numbers = []
for i in range(0,10):
    number = int(input(f"Enter {i+1} number:"))
    
    numbers.append(number)
    
print("Original List:", numbers)
print("Unique entered numbers:", set(numbers))
print("Unique no. of values:", len(set(numbers)))


#### Exercise 2

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Union: {A | B}")
print(f"Intersection: {A & B}")
print(f"Difference(A-B): {A-B}")
print(f"Difference(B-A): {B-A}")
print(f"Symmetric  Difference: {A^B}")


#### Exercise 3

sentence = input("Enter a sentence:")

words =  sentence.split()    
print(set(words))
    

    
#### Mini Challenge: Common Friends 

user1 = {"Ram", "Hari", "Sita", "Asha"}
user2 = {"Hari", "Asha", "Gita", "Nabin"}

print("Friends of user1: ",user1)
print("Friends of user2:" ,user2)

print("Mutual friends:", user1&user2)
print("Friends only User 1 has:", user1-user2)
print("Friends only User 2 has:", user2-user1)

print("Total unique friends:", len(user1|user2))    

