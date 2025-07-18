gradebook={}
def add_student(student_name):
  if student_name in gradebook:
    print("Student already exists")
  else:
    gradebook[student_name]=[]
    print("Student added")
def add_grade(student_name, grade):
  if student_name in gradebook:
    gradebook[student_name].append(grade)
    print(f"Grade {grade} added for {student_name}.")
  else:
    print("Student not found.")
def view_grades(student_name):
  if student_name in gradebook:
    print(f"--- Grades for {student_name} ---")
    if gradebook[student_name]:
      print(f"Grades: {', '.join(map(str, gradebook[student_name]))}")
    else:
      print(f"No grades recorded for {student_name}.")
  else:
    print(f"Student '{student_name}' not found.")
def calculate_average(student_name):
  if student_name in gradebook:
    if not gradebook[student_name]:
      return "No grades to calculate average."
    else:
      average = sum(gradebook[student_name]) / len(gradebook[student_name])
      return round(average, 2)
  else:
    return f"Student '{student_name}' not found."
while True:
  print("\n--- Student Gradebook Menu ---")
  print("1. Add Student")
  print("2. Add Grade for Student")
  print("3. View Grades for Student")
  print("4. Calculate Student Average")
  print("5. Exit")
  print("------------------------------")

  try:
    choice = int(input("Enter your choice: "))
    if choice ==1:
      name1=input("Student name: ")
      add_student(name1)
    elif choice ==2:
      name1=input("Student name: ")
      grade1 = float(input("student grade: "))
      add_grade(name1,grade1)
    elif choice == 3:
      name1=input("Student name: ")
      view_grades(name1)
    elif choice==4:
      name_for_average = input("Enter student name: ")
      result = calculate_average(name1)
      print(f"Average for {name_for_average}: {result}")
    elif choice == 5:
      print("Exiting Gradebook. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
  except ValueError:
    print("Invalid input. Please enter a number corresponding to a menu option (1-5).")