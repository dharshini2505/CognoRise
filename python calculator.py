def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def display_menu():
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
def input_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4): ")
    if choice in ("1", "2", "3", "4"):
        num1 = input_number("Enter the first number: ")

        num2 = input_number("Enter the second number: ")
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        answer = input("Do you want to continue? (yes/no): ")
        if answer.lower() == "no":
            break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
