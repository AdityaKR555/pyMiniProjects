operand1 = float(input("Enter first number: "))
operator = input("Choose Operator: + - * / % : ")
operand2 = float(input("Enter second number: "))

if operator == '+':
    print("Result = ", (operand1+operand2))

elif operator == '-':
    print("Result = ", (operand1-operand2))

elif operator == '*':
    print("Result = ", (operand1*operand2))

elif operator == '/':
    if operand2 == 0:
        print("Cannot divide by zero.")
    else:
        print("Result = ", (operand1/operand2))

elif operator == '%':
    print("Result = ", (operand1 % operand2))

else:
    print("Invalid operator")
    