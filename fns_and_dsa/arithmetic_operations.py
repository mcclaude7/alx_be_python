def perform_operation(num1, num2, operation):
    if operation == "add":
        return  num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid number"
    
x = float(input("Enter num1:"))
y = float(input("Enter num2:"))
z = input("Enter the operation (add, substract, multiply, divide): ").strip().lower()
print(perform_operation(x,y,z))
