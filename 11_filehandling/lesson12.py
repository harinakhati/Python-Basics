### Practice 

#### Exercise 1

with open("name.txt", "a") as file:
    name = input("Enter your name:")
    file.write(name)
    
    
#### Exercise 2

with open("name.txt", "r") as file:
    print(file.read())
   
    
#### Exerice 3


with open("movies.txt", "a") as file:
    for i in range(0,3):
        movie = input("Enter your favourite movie:\n")
        file.write(movie + "\n")
    
with open("movies.txt", "r") as file:
    print("All the favourite movies:", file.read())