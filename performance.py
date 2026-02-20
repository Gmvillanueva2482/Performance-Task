# To-Do List for Performance Task
# Purpose : To organize and prioritize tasks for the Performance Task


tasks = {                                           # This is our dictionary to store tasks based on their priority categories.
"Incidental" : [],
"Coordinated": [],
"Planned" : []
}

def add_new_task(task_name, priority):             # This fucntion adds a new task to the appropriate category based on the priority input by the user. 
    if priority == "1":
       tasks["Incidental"].append(task_name)
       print(f"Task '{task_name}' added to Incidental tasks.")
    elif priority == "2":
       tasks["Coordinated"].append(task_name)
       print(f"Task '{task_name}' added to Coordinated tasks.")
    elif priority == "3":
       tasks["Planned"].append(task_name)
       print(f"Task '{task_name}' added to Planned tasks.")
    else:
         print("Invalid priority, Please choose 1, 2, or 3.")


def display_task():                              # This function displays the current tasks in each category, showing the priority and the tasks under each category.
    print("\n--- Current To-Do List ---")
    for priority, task_list in tasks.items():
        print(f"\n{priority} Tasks:")
        if not task_list:
            print("(Empty)")
        else:
            for i, task in enumerate(task_list, 1):
                print(f"{i}.{task}")


def remove_task(priority, task_number):        # This function removes a task from the specified category based on the task number input by the user. It checks for valid priority and task number before removing the task.
    if priority == "1":
        category = "Incidental"
    elif priority == "2":
        category = "Coordinated"
    elif priority == "3":
        category = "Planned"
    else:
        print("Invalid priority.")
        return 
    
    if 0 < task_number <= len(tasks[category]):
        removed = tasks[category].pop(task_number - 1)
        print(f"Task '{removed}' removed successfully")
    else:
        print("Invalid task number.")




while True:                                            # This is the main Loop of the program, which continuously prompts the user for actions until they choose to exit. It handles user input for adding, removing, and displaying tasks, as well as exiting the program.
    print("\n==== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2, Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("choose an option (1-4):")         # This Line prompts the user to choose an option from the menu and stores their input in the variable "choice". The program will then execute the corresponding action based on the user's selection.
 


    if choice == "1":
        task_name = input("Enter the task name: ")
        print("Select Priority")
        print("1 - Incidental")
        print("2 - Coordinated")
        print("3 - Planned")
        priority = input("Enter priority (1-3): ")
        add_new_task(task_name, priority)


    elif choice == "2":
        display_task()
        print("Select Priority Category: ")
        print("1 - Incidental")
        print("2 - Coordinated")
        print("3 - Planned")
        priority = input("Enter priority (1-3): ")
        try:
            task_number = int(input("Enter task number to remove: "))
            remove_task(priority, task_number)

        except ValueError:
            print ("Please enter  valid number.")


    elif choice == "3":
        display_task()


    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4.")