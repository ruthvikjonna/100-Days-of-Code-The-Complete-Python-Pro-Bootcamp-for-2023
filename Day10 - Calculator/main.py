import os

logo = """
 _____________________
|  _________________  |
| | Ruthvik Jonna   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Addition
def add(n1, n2):
    '''This function adds two numbers.'''
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    '''This function subtracts two numbers.'''
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    '''This function multiplies two numbers.'''
    return n1 * n2

# Division
def divide(n1, n2):
    '''This function divides two numbers.'''
    return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))

    for key in operations:
        print(key)

    keep_going = True
    while keep_going != False:
        chosen_operation = input("Pick a mathematical operation: ")

        num2 = float(input("What's the next number? "))

        calculation = operations[chosen_operation]
        answer = calculation(num1, num2)

        print(f"{num1} {chosen_operation} {num2} = {answer}")

        keep_going_question = input(f"Type 'yes' to continue calculating with {answer}, type 'no' to start a new calculation, or type 'exit' to stop the program: ")

        if keep_going_question == "yes":
            num1 = answer
        elif keep_going_question == "no":
            keep_going = False
            os.system('cls')
            calculator()
        elif keep_going_question == "exit":
            keep_going = False

calculator()