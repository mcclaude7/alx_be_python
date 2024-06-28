x = int(input("Enter the first  number:"))
y = int(input("Enter the second number:"))
operation = input("Chose the operation (+, -, *, /):")

match operation:
    case ("+"):
        print("The result is",x+y)
    case ("-"):
        print("The result is",x-y)
    case ("*"):
        print("the result is", x*y)
    case ("/"):
        if (y>0):
            print("the result is",x/y)
        else:
            print("Cannot divide by zero.")

