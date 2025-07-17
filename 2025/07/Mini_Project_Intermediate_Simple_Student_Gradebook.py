gradebook={}
def add_student(student_name):
  if student_name in gradebook:
    print("Student already exists")
    pass
  else:
    gradebook[student_name]=[]
    print("Student added")
def add_grade(student_name, grade):
  if student_name in gradebook:
    gradebook[student_name].append(grade)
    print("Grade updated")
  else:
    print("Student not found.")
def view_grades(student_name):
  if student_name in gradebook:
    print("Name of the student is:",student_name)
    if gradebook[student_name]:
      print("Grades of the student:",gradebook[student_name])
    else:
      print("No grades recorded for this student.")
  else:
    print("Student not found.")
def calculate_average(student_name):
  if student_name in gradebook:
    print(gradebook[student_name])
    if gradebook[student_name]==[]:
      print("No grades to calculate average.")
    else:
      Averg= round((sum(gradebook[student_name])/len(gradebook[student_name])),2)
      return Averg
  else:
    print("Student not found.")
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
      print("You chose to Add Student.")
    elif choice ==2:
      name1=input("Student name: ")
      grade1 = float(input("student grade: "))
      add_grade(name1,grade1)
      print("You chose to Add Grades.")
    elif choice == 3:
      name1=input("Student name: ")
      view_grades(name1)
    elif choice==4:
      name1=input("Student name: ")
      if gradebook[name1]==[]:
        print("Error -No grades available for average")
      else:
        print(calculate_average(name1))
      print("You chose to Calculate Average.")
    elif choice == 5:
      print("Exiting Gradebook. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
  except ValueError:
    print("Invalid input. Please enter a number corresponding to a menu option (1-5).")