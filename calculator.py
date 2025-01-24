def add(a, b):
        return a + b 

def subtract(a, b):
        return a - b

def divide(a, b):
        if(b == 0):
            return "Error! Division by zero"
        return a / b

def multiply(a, b):
        return a * b

def calculator():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

while True:

        calculator()

        choice = input("Enter choice (1/2/3/4): ")


        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            # Ask the user if they want to make another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() =! 'yes':
                break
        else:
            print("Invalid input. Please choose a valid operation.")

# Run the calculator
   