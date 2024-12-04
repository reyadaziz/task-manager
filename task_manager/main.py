from task_manager1 import add_task, view_tasks, remove_task, search_task, update_task

while True:
  print("\n\nwelcome to Task manager:")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Remove Task")
  print("4. Search Task")
  print("5. Update Task")
  print("6. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    add_task(title, description, due_date)
    print("Task added successfully!")
  elif choice == "2":
    view_tasks()

  elif choice == "3":
       index = int(input("Enter the index of the task to remove: "))
       remove_task(index)  
       print("Task removed successfully")
  elif choice == "4" :
     query = input("Enter the search query: ")
     search_task(query)
  elif choice == "5":
     index = int(input("Enter the index of the task to update: "))
     update_task(index)   
     print("Task updated successfully!")
  else:
     break
print("Exiting Task Manager...")     