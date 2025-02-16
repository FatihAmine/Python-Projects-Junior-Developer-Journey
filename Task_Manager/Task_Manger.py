from ast import Delete
import csv
import os

filename = "Task Manager.csv"

# Add task function

def add_task():
    print('################# Welcome To Your Task Manager #################')
    title = input("Title of Task: ")
    description = input("Description of Task: ")
    start_date = input("Start Date of Task (YYYY-MM-DD): ")
    deadline = input("Deadline of Task (YYYY-MM-DD): ")  
    # Print info 
    task_info = f"\nTitle of Task: {title}\n" \
                f"Description: {description}\n" \
                f"Start Date: {start_date}\n" \
                f"Deadline: {deadline}"

    print(task_info)
    
    # Check if the file exists, if not, write headers
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists: 
            writer.writerow(['Title', 'Description', 'Start Date', 'Deadline'])
        writer.writerow([title, description, start_date, deadline])


# delete task

def remove_task():
    title_to_delete = input("Enter the title of the task you want to delete: ")


    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

 
    tasks = [row for row in rows if row[0] != title_to_delete]

    if len(tasks) < len(rows):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)     
    else:
        print(f"No task found with the title: {title_to_delete}")


# view task

def view_task():
    with open('Task Manager.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)  
        for row in reader:
            print(row) 

# Menu function

def user(menu):
    match menu:
        case 1:
            add_task()      
            return "Task added successfully!"
        case 2:
            remove_task()
            return "Task deleted successfully."
        case 3:
            view_task()
            return "This is your task"
        case _:
            return "There is an error"
    

try:
    menu = int(input("Enter a menu option (1-3): "))
    print(user(menu))

except ValueError:
    print("Invalid input. Please enter a number.")
