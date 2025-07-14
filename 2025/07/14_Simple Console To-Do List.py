tasks=[]
def add_task(task_description):
  task_dictionary = {'description': task_description, 'completed': False}
  tasks.append(task_dictionary)
  print(f"Task '{task_description}' added.")
def view_tasks():
  if tasks==[]:
    print("No tasks in the list.")
    return
  else:
    for index,task in enumerate(tasks,start=1):
      status="[X]" if task['completed'] else '[ ]'
      description = task['description']
      print(f'{index}.{status}{description}')
    print("\n--- Your To-Do List ---")
    print("-----------------------")
def mark_task_complete(task_index):
  actual_index=task_index-1
  if 0<=actual_index<len(tasks):
    task=tasks[actual_index]
    if task['completed']:
      print(f"task'{task['description']}' is already complete.")
    else:
      task['completed']=True
      print(f"task'{task['description']}' mark as complete.")
  else:
    print("Invalid task number. Please enter a valid number from the list.")
while True:
  print("\n--- To-Do List Menu ---")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Complete")
  print("4. Exit")
  print("-----------------------")
  try:
    choice = int(input("Enter your choice: "))
    if choice ==1:
      task_desc = input("Enter task description: ")
      add_task(task_desc)
    elif choice ==2:
      view_tasks()
    elif choice ==3:
      try:
        task_num = int(input("Enter task number to mark as complete: "))
        mark_task_complete(task_num)
      except ValueError:
        print("Invalid input for task number. Please enter a digit.")
    elif choice ==4:
      print("Exiting To-Do List. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")
  except ValueError:
    print("Invalid input. Please enter a number corresponding to a menu option.")