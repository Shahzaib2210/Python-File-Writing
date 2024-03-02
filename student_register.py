'''
# Pseudo Code
1 - Take input, the total number of student user want to register and
    convert it into integer and store in total_student variable.
2 - Run for loop from range(0,total_student).
3 - Every time take input from user student ID number and store in student_id_number variable.
6 - Now reg_form = open reg_form.txt file and write it.
7 - Write reg_form.write"Student Id Number: " + student_id_number + "\n" + "------------------------------\n") 
8 - Print message "Thank you, ID numbers saved to txt file reg_form"
'''
# Taking total number of student user want to register input.
total_student = int(input("Enter the number of student you want to registered : "))

for x in range(0, total_student): # Running for loop from 0 to total_student
   # Taking Student ID number input.
   student_id_number = input("Please enter student ID numbers: ")
   # Opening file.
   reg_form = open('reg_form.txt', 'a+') 
   # Writing on file.
   reg_form.write("Student Id Number: " + student_id_number + "\n" + "------------------------------\n") 
   # Print message.
   print ("Thank you, ID numbers saved to txt file reg_form")