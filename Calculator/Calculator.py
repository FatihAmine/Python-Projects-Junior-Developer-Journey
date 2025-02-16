def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    while True: 
        print('----------------- Welcome To Your Calculator -----------------')
        print('Choose the operation that you want:')
        print('Press 1 - Addition: Adds two numbers.')
        print('Press 2 - Subtraction: Subtracts one number from another.')
        print('Press 3 - Multiplication: Multiplies two numbers.')
        print('Press 4 - Division: Divides one number by another.')
        print('Press 5 - Exit: Exit the calculator.')

        try:
            operations = int(input("Enter a menu option (1-5): "))
            if operations == 5:
                print("Exiting the calculator. Goodbye!")
                break 

            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))

            match operations:
                case 1:
                    print('The Addition calculation of your two numbers is:', addition(a, b))
                case 2:
                    print('The Subtraction calculation of your two numbers is:', subtraction(a, b))
                case 3:
                    print('The Multiplication calculation of your two numbers is:', multiplication(a, b))
                case 4:
                    result = division(a, b)
                    if result == "Error: Division by zero":
                        print(result)
                    else:
                        print('The Division calculation of your two numbers is:', result)
                case _:
                    print('Invalid option. Please choose a valid operation.')

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# the calculator
calculator()
