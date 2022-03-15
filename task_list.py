tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


def make_list_readable(list, list_statement, list_index):
    if len(list) > 1:
        while (list_index < len(list)-1):
            list_statement += list[list_index] + ", "
            list_index += 1
        list_statement += f"and {list[-1]}."
    else:
        list_statement = list[0] + "."
    return list_statement.lower()



def get_uncompleted_tasks():
    uncompleted_tasks = []
    uncompleted_tasks_statement = ""
    task_number = 0
    for task in tasks:
        if task["completed"] == False:
            uncompleted_tasks.append(task["description"])
    print_statement = make_list_readable(uncompleted_tasks, uncompleted_tasks_statement, task_number)      
    print(f"You still need to {print_statement}")

def get_completed_tasks():
    completed_tasks = []
    completed_tasks_statement = ""
    task_number = 0
    for task in tasks:
        if task["completed"] == True:
            completed_tasks.append(task["description"])
    print_statement = make_list_readable(completed_tasks, completed_tasks_statement, task_number)
    print(f"You have already done these ones: {print_statement}")

def get_task_descriptions():
    task_descriptions = []
    task_descriptions_statement = ""
    task_number = 0
    for task in tasks:
        task_descriptions.append(task["description"])
    print_statement = make_list_readable(task_descriptions, task_descriptions_statement, task_number)
    print(f"Your to do list: \n{print_statement}")

def get_slow_tasks():
    slow_tasks = []
    slow_tasks_statement = ""
    task_number = 0
    time = input("Print out the tasks that take more than how many minutes? ")
    for task in tasks:
        max
        if int(task["time_taken"]) > int(time):
            slow_tasks.append(task["description"])
    if len(slow_tasks) == 0:        
        print("There are no chores that take that long.")
    else:
        print_statement = make_list_readable(slow_tasks, slow_tasks_statement, task_number)
        print(f"These tasks all take more than {time} minutes: {print_statement}")
    

def get_task_by_description():
    task_description = input("What task would you like to search for? ")
    task_found_status = False
    for task in tasks:
        if task_description.lower() == task["description"].lower() and task["completed"]== False:
            print(f'\'{task["description"]}\' has not been done yet and should take {task["time_taken"]} minutes.')
            task_found_status = True
        if task_description.lower() == task["description"].lower() and task["completed"] == True:
            print(f'\'{task["description"]}\' has already been done.')
            task_found_status = True
    if task_found_status == False:
        print(f"Sorry, I couldn't find \'{task_description}\' in your to do list.")
        

def mark_as_complete():
    task_description = input("What task would you like to mark as 'complete'? ")
    task_found_status = False
    for task in tasks:
        if task_description.lower() == task["description"].lower():
            task["completed"] = True
            task_found_status = True
    if task_found_status == True:
        print(f"{task_description} has been marked as 'complete'.")
    else:
        print(f"I'm sorry, I couldn't find \'{task_description}\' on your list.")
    
def add_a_task():
    task_description = input("What is the description of the task you would like to add? ")
    task_status_query = input("Has the task been completed? y/n ")
    task_time = input("How many minutes would you like to accolate for this task? ")
    if task_status_query == "y":
        task_status = True
    if task_status_query == "n":
        task_status = False
    tasks.append( {
        "description": task_description,
        "completed": task_status,
        "time_taken": task_time
    })
    print(f"{task_description} has been added to your list.")

def return_to_menu():
    input("Press M or m to return to the main menu. ")


option = ""
while option != "q":
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        get_task_descriptions()
        return_to_menu()
    
    if option == "2":
        get_uncompleted_tasks()
        return_to_menu()
    
    if option == "3":
        get_completed_tasks()
        return_to_menu()

    if option == "4":
        mark_as_complete()
        return_to_menu()

    if option == "5":
        get_slow_tasks()
        return_to_menu()
    
    if option == "6":
        get_task_by_description()
        return_to_menu()

    if option == "7":
        add_a_task()
        return_to_menu()
    