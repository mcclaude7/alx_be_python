num1 = float(input("Enter 1st number: "))
operation = input("Enter your desired sign to perform your operation(+, -, x, /):")
num2 = float(input("Enter 2nd number: "))

if (operation == "+"):
    print(f"the sum of {num1} and {num2} is {num1+num2}")
elif (operation == "-"):
    sub = num1 - num2
    print(f"The substraction of {num1} and {num2} is {sub}")
elif (operation == "x"):
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
elif (operation == "/"):
    div = num1 / num2
    print(f"The division of {num1} and {num2} is {div}")
else:
    print("Invalid operation")