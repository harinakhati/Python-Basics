#### Practice 

### Exercise 1

import geometry

side = int(input("Enter the side of square:"))
geometry.area_square(side)

length = int(input("Enter length of rectangle:"))
width = int(input("Enter width of rectangle:"))
geometry.area_rectangle(length,width)  


### Exercise 2

import random

side = random.randint(1,6)
print("You rolled:", side)



### Exercise 3

from math import sqrt, ceil, floor

number = int(input("Enter a number:"))
print(f"Square root: {sqrt(number)}")
print(f"Ceiling: {ceil(sqrt(number))}")
print(f"Floor: {floor(sqrt(number))}")

