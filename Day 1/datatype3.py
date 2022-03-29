"""Write a program that takes Student's name and their marks in 3 subjects as input. 
Print each student's total marks as output.
"""

no_of_student = int(input("Enter Total number of students : "))

for i in range(no_of_student):
    name = input("Enter Student name : ")
    subject1 = int(input("Enter marks in subject 1 : "))
    subject2 = int(input("Enter marks in subject 2 : "))
    subject3 = int(input("Enter marks in subject 3 : "))
    students = {}
    students[i] = {"name":name,"subject1":subject1,"subject2":subject2,"subject3":subject3}
    
    total_marks = 0
    for j in students:
        total_marks = students[j].get("subject1") + students[j].get("subject2") + students[j].get("subject3")
        print("Total marks of %s is %s." % (students[j].get("name"), total_marks))

    