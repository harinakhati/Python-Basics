## Example

laptop = {
    "brand" : "Dell",
    "model" : "Latitude E5470",
    "ram" : "16 GB",
    "storage": "512 GB SSD",
    "processor" : "Inter Core i5"
}

for key, value in laptop.items():
    print(f"{key} : {value}")
    
    
## Mini Challenge Student Record System

student = {}

student['name'] = input("Enter name:")
student['age'] = int(input("Enter age:"))
student['program'] = input("Enter program:")

print("\nStudent Information")

for key, value in student.items():
    print(f"{key} : {value}")


#### Practice 

### Exercise 1

book = {
    "title": "The Stranger",
    "author": "Franz Kafka",
    "price": 400
}

for key, value in book.items():
    print(f"{key} : {value}")



### Exercise 2

person = {}

person['Name'] = input("Enter name:")
person['Age'] = int(input("Enter age:"))
person['City'] = input("Enter city:")


print("\nPerson's Details")
for key, value in person.items():
    print(f"{key} : {value}")


### Exercise 3

marks = {
    "Harina": 90,
    "Asha": 85,
    "Ram": 78,
    "Sita": 95,
    "Hari": 88
}

name = input("Enter name:").strip()

for key in marks.keys():
    if name == key:
        print(f"\nMarks of {name} is {marks.get(name)}")
    else:
        print("Student not found.")