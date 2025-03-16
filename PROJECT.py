
import os


def main():
  
  #Repeats code if input is not in range (0-9)
  while True:
    
      os.system('cls')
      print (
            """
            Student Informaiton System
            ==========================

              [1] Add Student details
              [2] Update a Student inforamtion
              [3] Delete a Student
              [4] List Registered Students
              [5] Find a Student by StudentID
              [6] Find a Student by a Given Parent Name
              [7] Find Students With Grade Letter A
              [8] Find Students With Grade 60 - 69
              [9] Students Statistics

              [0] Exit
            """
          )


      try:
        #Asks user to input a number
        mode_choice = int(input("\tEnter Your Choice : "))

        #add student
        if mode_choice == 1:
          print("\n\nStudent Information System - Add Student Details")
          print("="*48 + '\n')
          add_student()
        
        #Update student info
        elif mode_choice == 2:
          print("\n\nStudent Information System - Update a Student inforamtion")
          print("="*57 + '\n')
          input_id = input("Enter Student ID: ")
          update_books(input_id)

        #Delete Student info
        elif mode_choice == 3:
          print("\n\nStudent Information System - Delete a Student")
          print("="*45 + '\n')
          input_id = input("Enter Student ID to delete: ")
          delete_student(input_id)

        #list registered students
        elif mode_choice == 4:
          print("\n\nStudent Information System - List Registered Students")
          print("="*53 + '\n')
          list_students()

        #Find a Student by StudentID
        elif mode_choice == 5:
          print("\n\nStudent Information System - Find a Student by StudentID")
          print("="*56 + '\n')
          input_id = input("Enter Student ID to find : ")
          find_st_id(input_id)

        #Find a Student by a Given Parent Name
        elif mode_choice == 6:
          print("\n\nStudent Information System - Find a Student by a Given Parent Name")
          print("="*66 + '\n')
          input_parent = input("Enter Parent Name: ")
          find_st_parent(input_parent)

        #Find Students With Grade Letter A
        elif mode_choice == 7:
          print("\n\nStudent Information System - Find Students With Grade Letter A")
          print("="*63 + '\n')
          gradeletter = 'A'
          grade_A(gradeletter)

        #Find Students With Grade Letter 60 to 69
        elif mode_choice == 8:
          print("\n\nStudent Information System - Find Students With Grade Letter 60 to 69")
          print("="*69 + '\n')
          grade_60to69()
        
        #list student statistics  
        elif mode_choice == 9:
          print("\n\nStudent Information System - Students Statistics")
          print("="*48)
          statistics()

        #exit/close program
        elif mode_choice == 0:
          print("\n\nSee you next time, Goodbye\n")
          break

        else:
          input("\n[ Please enter a value between 0-9, press [ Enter ] to try again ] ")

      except ValueError:  
        input("\n[ Please enter a value between 0-9, press [ Enter ] to try again ] ")


#A Function that asks the user to input data of a new
#Student and then add the data to Students.txt
#Seperating the fields with the same '|' character.
#The function makes sure that the student ID is not already in stock
def add_student():

  #Opens Students.txt as read
  txt_file = open("Students.txt",'r')
  #reads each line in Students.txt
  st_list = txt_file.readlines()

  #Asks user to input Student ID in a specific format
  id = input("Enter new Student ID to add in the format [xx1234] : ")
  id = id_validation(id)

  #Looks at each individual line
  for student in st_list:

    #seperates line into each variable
    st_id, st_name, parent_name, borrowed, dob, grade = student.split('|',6)

    #finds out if student id already exists
    if id == st_id:
      print("\nStudent already exists....\n")
      break

  else:
    #if student id doesn't exist. . .
    #makes sure the input is valid
      
        #asks user for the new student's name
        st_name = input("Enter new student's name : ")
        #makes sure student name doesn't contain digits and isn't empty
        st_name = name_validation(st_name)

        #asks user to input parent's name
        parent_name = input("Enter new student's parent name : ")
        #makes sure parent name doesn't contain digits and isn't empty
        parent_name = name_validation(parent_name)

        #repeats program if ValueError
        while True:
          try:
            #asks user for number of books borrowed (Cannot be a negative)
            borrowed = int(input("Please enter number of borrowed books : "))
            if borrowed<0:
              borrowed = int(input("Error, number of borrowed books can't be negative, Please enter a valid number : "))
            else:
              break

          except ValueError:
            input("Number of borrowed books can only be numeric, Press [ Enter ] to try again ")
            print()

        #repeats if date is not correct format or does not make sense
        while True:
          #asks user for DOB
          dob = input("Enter date of birth in the format dd-mm-yyyy (e.g 31-12-2022) : ")

          #checks if DOB is in the correct format
          #checks if DOB is numeric
          if dob[0:2].isdigit() == False or dob[3:5].isdigit() == False or dob[6:10].isdigit()==False:
            print("Date of birth can only be numeric")
          
          #makes sure dob is in the correct length
          elif len(dob) != 10:
            print("Date must be in the correct format dd-mm-yyyy (e.g 31-12-2022)")
          
          #makes sure date is correct
          elif dob == "00-00-0000":
            print("Date must be in the correct format dd-mm-yyyy (e.g 31-12-2022)")
            
          #checks if it is the correct format
          elif dob[2] != "-" and dob[5] != "-":
            print('Date must be in the correct format dd-mm-yyyy (e.g 31-12-2022)')
          
          #if month > 12
          elif int(dob[3:5]) > 12:
            print('Month must be between 0 and 12')

          #makes sure specific month is not greater than 31 days
          elif (int(dob[3:5]) == 1 or int(dob[3:5]) == 3 or int(dob[3:5]) == 5 or int(dob[3:5]) == 7 or int(dob[3:5]) == 8 or int(dob[3:5]) == 10 or int(dob[3:5]) == 12) and (int(dob[0:2])>31):
            print(f'Month {dob[3:5]} cannot have more than 31 days')

          #makes sure specific month is not greater 30 days
          elif (int(dob[3:5]) == 4 or int(dob[3:5]) == 6 or int(dob[3:5]) == 9 or int(dob[3:5]) == 11) and (int(dob[0:2]) > 30):
            print(f'Month {dob[3:5]} cannot have more than 30 days')

          #makes sure month febuary does not have 28 days (non leap) or 29 days(leap)
          #if it is a century
          elif int(dob[8:10]) == 00:
            #if centure is divisable by 400 then leap year
            if int(dob[6:10])%400 == 0:
              if int(dob[3:5]) == 2 and int(dob[0:2]) > 29:
                print('Day cannot be more than 29 in a leap year')
              else:
                break
            #makes sure year is realistic (1900-2022)  
            elif int(dob[6:10]) > 2022 or int(dob[6:10]) < 1900:
              print('Year must be between 1900 and 2022 ')

          #if not century and divisable by 4 then leap year
          elif int(dob[6:10])%4 == 0:
            if int(dob[3:5]) == 2 and int(dob[0:2]) > 29:
              print('Day cannot be more than 29 in a leap year')
            else:
              break

          #not leap year
          elif int(dob[3:5]) == 2 and int(dob[0:2]) > 28:
            print('non leap year cannot be more than 28 days')
          
          #makes sure year is realistic (1900-2022)
          elif int(dob[6:10]) > 2022 or int(dob[6:10]) < 1900:
            print('Year must be between 1900 and 2022 ')
          else:
            break
        
        #makes sure value is integer
        while True:
          try:
            #asks user for their grade (muse be between 0 and 100)
            grade = int(input("Enter semester grade : "))
            while grade < 0 or grade > 100:
                grade = int(input("Grade must be between 0 and 100, please try again : "))
            break
          except ValueError:
            input("Grade can only be numeric, press [ Enter ] to try again")
            print()


        new_header = '\nNew Student Profile:\n' + '='*20
        #variable new_student for diplay in the console
        new_student = f'{id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
        #variable to input data into Students.txt
        new_student1 =  f'{id}|{st_name}|{parent_name}|{borrowed}|{dob}|{grade}'

        print(new_header)
        header()
        print(new_student)
        print("\n.......Record added.")

        txt_file.close()

        #opens Students.txt as append to insert the new data
        txt_file = open("Students.txt",'a')
        txt_file.write(new_student1 + '\n')
        txt_file.close()
             
  input("\nPress [ Enter ] to continue ")

#Function that takes as parameter the student ID to be updated.
#If the student ID is found in the file, the function promts the 
#user the number of books (i.e, number of compies) to be borrowed/returned
#It checks that a student cannot borrow more than 2 books at a time
def update_books(input_id): 
  #opens Students.txt as read and temp.txt as write
  txt_file = open("Students.txt",'r')
  temp_file = open('temp.txt','w')

  #reads each line in Students.txt
  st_list = txt_file.readlines()
  #boolean for student exists
  st_exists = False

  #looks at each individual line in Students.txt
  for student in st_list:
    
    #seperate line into each variable
    st_id, st_name, parent_name, borrowed, dob, grade = student.split('|',6)
    updated_header = '\n\nHere Is Your Updated Profile:\n' + '='* 29 + '\n'
    grade = grade.rstrip()

    #checks if student ID exists
    if input_id == st_id:
      st_exists = True
      #repeat if input is not b or r
      while True:
        #asks user if they want to borrow or return a book
        service = input("Do you want to Borrow(b) or Return(r) : ")
        #takes first character of service
        if len(service.strip()) == 1:
          service = service.lower()
          if service == 'b' or service == 'r':
            break
          else:
            print("Please enter either b or r")
        else:
          print("Please enter either b or r")
          

      #converts string into int
      borrowed = int(borrowed)

      #student does exist


      #makes sure the input is valid
      try:

        #only if user chose to borrow books
        if service == 'b':
          #Repeats if user borrowed more than 2 books or negative number
          while True:
            num_of_books = int(input("Enter the number of books to be borrowed : "))

            #number of books should be less than 3 and not a negative
            if num_of_books > 2 :
              print("\nSorry you can't borrow more than 2 books at a time......")
              temp_file.write(student)
              break

            elif num_of_books < 0:
              print("\nERROR, number of books borrowed cant be negative......")
              temp_file.write(student)
              break

            else:
              #updates number of books borrowed
              borrowed += num_of_books
              print(updated_header)
              header()
              updated_student = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
              print(updated_student)
              updated_student1 =  f'{st_id}|{st_name}|{parent_name}|{borrowed}|{dob}|{grade}'
              temp_file.write(updated_student1 + '\n')
              break
              

        #onlf if user chose to return books
        elif service == 'r':
          
          #repeat if number of books returned is less than borrowed book and is negative
          while True:
            num_of_books = int(input("Enter the number of books to be returned : "))

            #makes sure number of books returned is less than borrowed books and is not negative
            if num_of_books > borrowed:
              print("\nERROR, You cant return more books than you borrowed......")
              temp_file.write(student)
              break
            
            elif num_of_books < 0:
              print("\nERROR, number of books borrowed cant be negative......")
              temp_file.write(student)
              break
          
            else:
              #updates number of books borrowed
              borrowed -= num_of_books
              print(updated_header)
              header()
              grade = grade.rstrip()
              updated_student = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
              print(updated_student)
              updated_student1 =  f'{st_id}|{st_name}|{parent_name}|{borrowed}|{dob}|{grade}'
              temp_file.write(updated_student1 + '\n')  
              break          

      except ValueError:
        print("\nERROR number of books borrowed can only be numeric")
        temp_file.write(student)

    else:
      temp_file.write(student)   
  


  #is student does not exist...
  if st_exists == False:
    print("\nStudent doesn't exist......")
  else:
    pass
  #closes both file
  txt_file.close()
  temp_file.close()

  replace_file()
  input("\nPress [ Enter ] to continue ")

#function that takes as parameter the student ID of the student to be deleted
def delete_student(input_id):
  #opens Students.txt as read
  txt_file = open("Students.txt",'r')
  #reads each line in Students.txt
  st_list = txt_file.readlines()
  #opnes temp.txt as write
  temp_file = open("temp.txt", 'w')
  #list for the deleted student name and id
  deleted_student = []
  #boolean for student exists
  st_exists = False

  #looks at each individual lin in Students.txt
  for student in st_list:
    #split line into 2 variables (only looking at Student ID)
    st_id, st_name, others = student.split('|',2)

    #finds out if id == st_id
    #if so, do not write the student info in temp.txt
    if input_id != st_id:
      temp_file.write(student)
    
    #if the input id exists it appends the name and id of the student to the deleted_student list
    elif input_id == st_id:
      st_exists = True
      deleted_student.append(st_id)
      deleted_student.append(st_name)

  #close both files
  txt_file.close()
  temp_file.close()

  #output correct message if student is found
  if st_exists == True:
    replace_file()
    print(f'\n{deleted_student[1]} ({deleted_student[0]}) has been deleted from the system.....')

  else:
    print("Student Does Not Exist.....")

  input("\nPress [ Enter ] to continue ")

#Function that lists the registered student list in a nice
#Tabular format.
def list_students():
  #opens Students.txt as read
  txt_file = open("Students.txt",'r')
  #reads each line in students.txt
  st_list = txt_file.readlines()
  header()

  for student in st_list:
    st_id, st_name, parent_name, borrowed, dob, grade =  student.split('|',6)
    
    #does not print the header that is in Students.txt
    if "books" in student:
      pass

    else:
      #prints student inforamtion
      grade = grade.rstrip()
      student_info = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
      print(student_info.rstrip())
  
  #closes Student.txt
  txt_file.close()

  input("\nPress [ Enter ] to continue ")

#Function that displays all the details of 
#registered student, searched by student ID
#the student ID should be entered as an 
#argument to the funtion
def find_st_id(input_id):
    
    #opens Students.txt as read
    txt_file = open("Students.txt",'r')
    #read each individual lin in Students.txt
    st_list = txt_file.readlines()

    for student in st_list:
      #split line into each variables
        st_id, st_name, parent_name, borrowed, dob, grade =  student.split('|',6)

        #if student id is found
        if input_id == st_id:
          #print student info
          grade = grade.rstrip()
          student_info = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
          profile_header = '\nStudent Profile:\n' + '='* 16 + '\n'
          print(profile_header)
          header()
          print(student_info)
          break

    else:
        print("\nStudent does not exist.....")

    #closes Students.txt
    txt_file.close()

    input("\nPress [ Enter ] to continue ")

#Function that produces a list of all students by a given parent name.
#Parent name entered as an arguement to the function
def find_st_parent(input_parent):

  #opens Students.txt as read
  txt_file = open("Students.txt",'r')
  #reads each line in Students.txt
  st_list = txt_file.readlines()
  
  #looks at each individual line 
  for student in st_list:
    #splits line into each variable
    st_id, st_name, parent_name, borrowed, dob, grade =  student.split('|',6)

    #Compares if parent name is the same
    #Prints student info that has the same parent name
    if input_parent.rstrip().lstrip().lower() == parent_name.rstrip().lstrip().lower():
      grade = grade.rstrip()
      student_info = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
      profile_header = '\nStudent Profile:\n' + '='* 16 

      print(profile_header)
      header()
      print(student_info)
      break 
  #if Parent is not found
  else:
      print("\nParent does not exist....\n")

  #closes Students.txt
  txt_file.close()

  input("\nPress [ Enter ] to continue ")

#Function that produces a list of all students that 
#Have the grade letter A.
def grade_A(A):
  
  #Opens Students.txt as Read
  txt_file = open("Students.txt",'r')
  #Reads each line in Students.txt
  st_list = txt_file.readlines()
  #list for all students with grade A
  st_A = []
  #variable to check if there is any grade A students by couting
  a = 0

  #looks at each individual line in Students.txt
  for student in st_list:
    #splits line into each variable
    st_id, st_name, parent_name, borrowed, dob, grade =  student.split('|',6)

    try:
      #boolean for values greater than or equal to 90
      if A == grade_letter(grade):

      #if grade is >= 90 then append list st_A with that students info
        grade = grade.rstrip()
        student_info = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
        st_A.append(student_info)
        a+=1

      else:
        pass
    except ValueError:
      pass
  
  #close Students.txt
  txt_file.close()

  #prints suitable message
  if a > 0:
    print ('\nThe Students with the grade A are:')
    print("="*34 + '\n')
    header()

    for student in st_A:
      print (student)

  else:
    print("No student with the grade A")
  
  input("\nPress [ Enter ] to continue ")

#Function that produces a list of all students whose grades are >= 60 and <70
def grade_60to69():

  #Open Students.txt as read
  txt_file = open("Students.txt",'r')
  #Reads each line in Students.txt
  st_list = txt_file.readlines()
  #list for all students with grade D
  st_D = []
  #Counter for all Students wit grade D
  d = 0

  #reads each individual lin in Students.txt
  for student in st_list:
    #splits line into each variable
    st_id, st_name, parent_name, borrowed, dob, grade =  student.split('|',6)


    try:
      #boolean for students with grades >=60 and <70
      D = 70>int(grade)>=60

      if D == True:
      #If grade is >=60 and <70 append list st_D with the students information
        grade = grade.rstrip()
        student_info = f'{st_id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{grade_letter(grade):^16}'
        st_D.append(student_info)
        d += 1

      else:
        pass
    except ValueError:
      pass


  
  #close Students.txt
  txt_file.close()

  #Outputs suitable message
  if d > 0:
    print ('The Students with the grade 60 to 69 are:')
    print('='*41 + '\n')
    header()

    for student in st_D:
      print (student)

  else:
    print("No student with the grade 60 to 69")

  input("\nPress [ Enter ] to continue ")

#Function that produce students' statistics such as:
#the passing rate, the failure rate, the best
#student grade, the least student grade
def statistics():
  #opens Students.txt as read
  txt_file = open("Students.txt",'r')
  #reads each line in Students.txt
  st_list = txt_file.readlines()
  #total students
  st_total = 0
  #passing rate
  passed = 0
  #failure rate
  failed = 0
  #best student grade
  best_grade = 0
  #least student grade
  least_grade = 100

  
  #looks at each individual line in Students.txt
  for student in st_list:
    
    #splits line into each variable
    st_id, st_name, parent_name, borrow, dob, grade =  student.split('|',6)

    try:
      #converts from string to int
      grade = int(grade)
      #append total students
      st_total += 1

      #append each variable according to students information
      if grade >= 50:
        passed += 1

      else:
        failed += 1

      if grade > best_grade:
        best_grade = grade

      if grade < least_grade:
        least_grade = grade

    except ValueError:
      pass
  
  #finds percentage of pass and fail rates
  pass_rate = (passed/st_total) * 100
  fail_rate = (failed/st_total) * 100

  #displays list in a tabular manner
  print (f'''
  Statistics:
  ===========
  The passing rate is : {round(pass_rate,2)}%
  The failing rate is : {round(fail_rate,2)}%
  The best grade is   : {best_grade:^5}
  The least grade is  : {least_grade:^5}
  ''')

  #closes Students.txt
  txt_file.close()

  input("\nPress [ Enter ] to continue ")

#function to identify grades of students
def grade_letter(grade):

    if 100>=int(grade)>=90:
            gradeletter='A'

    elif 90>int(grade)>=80:
            gradeletter='B'

    elif 80>int(grade)>=70:
        gradeletter='C'

    elif 70>int(grade)>=60:
        gradeletter='D'

    elif 60>int(grade)>=0:
        gradeletter='F'
        
    return gradeletter

#function that displays the header of Students.txt (first line)
def header():
  txt_file = open("Students.txt",'r')
  st_list = txt_file.readline()
  id, st_name, parent_name, borrowed, dob, grade =  st_list.split('|',6)
  grade = grade.strip('\n')
  display_header = f'{id:^15}|{st_name:^15}|{parent_name:^15}|{borrowed:^16}|{dob:^15}|{grade:^17}|{"Grade Letter":^17}'

  print(display_header.rstrip())

#function that makes sure student ID is in the correct format
def id_validation(id):
  #makes sure length is 6 characters and first 2 characters are alphabetical and last 4 are numeric
  while len(id)!=6 or id[0:2].isalpha() == False or id[2:6].isdigit() == False:
    id = input("Please enter the id in the following format [xx1234] : ")
  return id
    
#function that makes sure student/parent name has no digits and isn't empty
def name_validation(name):
  numbers = ["0", "1", "2", "3", "4", "5" ,"6" ,"7" ,"8" , "9"]
  #appends a number if the name input contains any digit
  num_check = [number for number in numbers if number in name]

  while True:
    num_check = [number for number in numbers if number in name]

    #checks if the name contains numeric values
    if num_check != []:
      name = input("Error, Name can't contain numbers please try again : ")
        
    #checks if the name is empty    
    elif name.isspace() or name == '':
      name = input("Error, Name can't be empty please try again : ")

    else:
      break

  return name

#replaces Students.txt with temp.txt
def replace_file():
  os.remove("Students.txt")
  os.rename('temp.txt', "Students.txt")


#start program
main()