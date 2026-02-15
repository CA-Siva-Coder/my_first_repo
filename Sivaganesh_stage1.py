#input from user
A = int(input("Enter first number:"))
B = int(input("Enter second number:"))
C = input("Enter operator (+, -, *, /):")

#calculation
if C == "+":
    result = A+B
    print("Result:",result)
elif C == "-":
    result = A-B
    print("Result:", result)
elif C =="*":
    result = A*B
    print("Result:", result)
elif C =="/":
    if B == 0:
         print("Error!!: Division by zero is not allowed")
    else:
        result = A/B
        print("Result:", result)
else:
    print("Invalid operator")
    