## Practice 

#### Exercise 1

months = ("Janaury", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print(f"First month of the year is {months[0]}.")
print(f"Last month of the year is {months[-1]}.")
print(f"Total no. of months is {len(months)}.")


#### Exercise 2

numbers = (10, 20, 30, 40, 50)

print(f"Second element: {numbers[1]}")
print(f"Last element: {numbers[-1]}")
print(f"Middle three elements: {numbers[1:4]}")


#### Exercise 3

def calculate(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    
    return total, average

numbers = [10, 20, 30]

total, average = calculate(numbers)

print(total)
print(average)


#### Mini challenge

student = ("Harina", 20, "Computer Science")

for info in range(len(student)):
    print(student[info])