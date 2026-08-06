## Mini Challange : To-Do List




def display_menu():
    print("\n==== TO-DO LIST ====")
    print("1. View Task")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\nYour Tasks:")
    
    for index, task in enumerate(tasks, start=1):
        if task['completed']:
            status = "Completed"
        else:
            status = "Pending"
            
        print(f"{index}. {task['task']} [{status}]")
        
def add_task(tasks):
    task = input("Enter task:").strip()
    if not task:
        print("Task cannot be empty.")
        return
    
    tasks.append({
        "task" : task,
        "completed" : False
    })
    
    print("Task added successfully.")

def complete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    view_tasks(tasks)
    
    try:
        task_number = int(input("Ebter task number:"))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    index = task_number - 1
    
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    
    tasks[index]["completed"] = True
    
    print("Task marked as completed.")

def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    index = task_number - 1
    
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    
    tasks.pop(index)
    print("Task deleted successfully.")
    
    
    
def main():
  tasks = [
    {"task": "Study Python", "completed": False},
    {"task": "Exercise", "completed": True}
  ]
  while True:
        choice = input("Choose an option:").strip()
        
        if choice == "1":
            view_tasks(tasks)
            
        elif choice == "2":
            add_task(tasks)
            
        elif choice == "3":
            complete_task(tasks)
                    
        elif choice == "4":
            delete_task(tasks)
            
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Feature not implemeneted yet.")
            
            
#Function call
main()
