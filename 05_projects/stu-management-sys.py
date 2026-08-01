class Student:
    
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program
        
    def display(self):
        print("\nStudent Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Program: {self.program}")
        

student = Student(
    input("Name:"),
    int(input("Age:")),
    input("Program:")
)

student.display()

