class Student:
    def __init__(self, name, age, program):
        self.name = name 
        self.age = age 
        self.program = program 
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Program: {self.program}")
        
def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty.")
        else:
            return value
        
def get_valid_age(message):
    while True:
        try:
            age = int(input(message))

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                return age

        except ValueError:
            print("Please enter a valid age.")

def find_student(students, search_name):
    for student in students:
        if student.name.lower() == search_name.lower():
            return student
    return None

    
def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                f"{student.name}, {student.age}, {student.program}\n"
            )

def load_students():
    students = [
    Student("Harina", 20, "BSc CSIT"),
    Student("Asha", 21, "BCA")
]
    try:
        with open("students.txt", "r") as file:
            
            for line in file:
                line = line.strip()
                
                if line:
                    name,age, program = line.split(",")
                    
                    students.append(
                        Student(
                            name,
                            int(age),
                            program
                            )
                    )
    except FileNotFoundError:
        pass
    return students

 
def display_menu():
    print("\n==== STUDENT RECORD SYSTEM ====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student(students):
    print("\n---- Add Student ----")

    name = get_non_empty_input("Enter name:")
    age = get_valid_age("Enter Age:")
    program = get_non_empty_input("Enter Program:")
    
    student = Student(name, age, program)
    students.append(student)
    
    print("Student added successfully.")

    
def view_student(students):
    print("\n=== Student Records ===")
    
    if len(students) == 0:
        print("No students available.")
        return
    
    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        student.display()


def search_student(students):
    print("\n---- Search Student ----")
    
    if len(students) == 0:
        print("No students available.")
        return
    
    search_name = input("Enter student name:").strip()
    student = find_student(students, search_name)
    
    if student:
        print("\nStudent found:\n")
        student.display()
        return
    else:        
        print("Student not found.")



def update_student(students):
    print("\n---- Update Student ----")
    if len(students) == 0:
            print("No students available.")
            return
        
    search_name = input("Enter student name:").strip() 
    student = find_student(students, search_name)
    
    for student in students:
        if student.name.lower() == search_name.lower():
            print("\nCurrent Information:\n")
            student.display()
            
            print("\nEnter New Details")
            student.name = get_non_empty_input("Enter New Name: ")
            student.age = get_valid_age("Enter New Age: ")
            student.program = get_non_empty_input("Enter New Program: ")
                        
            print("\nStudent Details updated successfully.")
            return 
    
    if student is None:           
        print("Student not found.")
        return
    

def delete_student(students):
    print("\n---- Delete Student ----")
    
    if len(students) == 0:
        print("No Students available.")
        return
    
    search_name = input("Enter student name:").strip()
        
    student = find_student(students, search_name)
    
    for student in students:
            # if student.name.lower() == search_name.lower():
            #     print("\nStudent found:\n")
            #     student.display()
            #     return
            
            confirm = input("\nAre you sure? (y/n):").lower()
            
            if confirm == "y":
                students.remove(student)
                print("\nStudent deleted successfully.")
            else:
                print("\nDeletion cancelled.")
            return
    
    if student is None:
        print("Student not found.")
        return

def main():
    students = load_students()
    
    while True:
        display_menu()
        choice = input("\nChoose an option:")
        
        if choice == "1":
            view_student(students)
            
        elif choice == "2":
            add_student(students)
            
        elif choice == "3":
            search_student(students)
            
        elif choice == "4":
            update_student(students)
            
        elif choice == "5":
            delete_student(students)
            
        elif choice == "6":
            print("\nThank you for using the Student Record System.")
            break
        
        else:
            print("Invalid choice.")
            
            
if __name__ == "__main__":
    main()