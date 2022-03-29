"""Create a program to take student information as input. 
Student will have First Name, Last Name, Roll No. Write a function 
to sort the list based on given input parameter. 
Input Parameters can be: ‘By First Name’ or ‘Last Name’ or ‘Roll No’.
"""

no_of_student = int(input("Enter number of student : "))

students = []

for i in range(no_of_student):
    fname = input("Enter First name :")
    lname = input("Enter Last name :")
    roll_no = int(input("Enter Roll no :"))
    students.append([fname,lname,roll_no])
    
    sorting_parameter = input("Enter Sorting parameter: ")
    if sorting_parameter == "fname":
        students.sort(key=lambda x: x[0])
    elif sorting_parameter == "lname":
        students.sort(key=lambda x: x[1])
    elif sorting_parameter == "roll":
        students.sort(key=lambda x: x[2])
        
print(students)        
    
