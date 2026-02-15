#input of marks from the student
Name = input("Name of the student:")

#let A,B & C be the 3 subjects
Audit = int(input("Enter your marks in Audit:"))
Accounts = int(input("Enter your marks in Accounts:"))
Costing = int(input("Enter your marks in Costing:"))

#Calculation of marks percentage
Total_marks = Audit+Accounts+Costing
print("Total marks:", Total_marks,"/300")
Percentage =int((Total_marks/300)*100)
print("Percentage of marks:", Percentage,"%")

#Grade of students
if Percentage>=75:
    print("Grade A")
elif Percentage>=60:
    print("Grade B")
elif Percentage>=40:
    print("Grade C")
else:
    print("Grade F")