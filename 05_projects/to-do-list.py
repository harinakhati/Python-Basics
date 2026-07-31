## Mini Challange : To-Do List

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")
    
    
    choice = input("Choose an option:").strip()
    
    if choice == "1":
        task = input("Enter task:").strip()
        tasks.append(task)
        print("Task Added.")
        
    elif choice == "2":
        if len(tasks) == 0:
            print("Task not available.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(f" {i+1}.{tasks[i]}")
                
    elif choice == "3":
        if len(tasks) == 0:
                    print("Task not available.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
                
            index = int(input("Enter task number:"))-1
            
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed Tasks: {removed}")
            else:
                print("Invalid task number.")
                
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")

