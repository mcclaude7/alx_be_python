from arithmetic_operations import perform_operation
def main():
    print("arithmetic operation")
    num1 = float(input("Enter num1:"))
    num2 = float(input("Enter num2:"))
    operation = input("Enter the operation (add, substract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

     