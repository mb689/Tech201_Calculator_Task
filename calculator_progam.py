# Calculator Program

# Function to ask user for what operator they want
def ask_user_for_operator():
    while True:
        operator = input("What operator would you like to do (+, -, /, *) or 00 to quit")
        if operator == "+" or operator == "*" or operator == "/" or operator == "-":
            break
        else:
            print("Please pick a valid operator")
    return operator

def ask_user_for_number1():
    while True:
        num1 = input("Pick your first number or 00 to quit ")
        if num1.isdigit():
            break
        else:
            print("Input is not a valid digit")
    return int(num1)


def ask_user_for_number2():
    while True:
        num2 = input("Pick your second number or 00 to quit ")
        if num2.isdigit():
            break
        else:
            print("Input is not a valid digit")
    return int(num2)


def calculator(int1: int, int2: int, operator: str) -> int:
    if operator == "/":
        return int1 / int2
    elif operator == "+":
        return int1 + int2
    elif operator == "-":
        return int1 - int2
    else:
        return int1 * int2

answer = calculator(ask_user_for_number1(), ask_user_for_number2(), ask_user_for_operator())
print(f"The answer is {answer}")

repeat = True

while repeat:
    # print(f"This is your answer {calculator(ask_user_for_number1(), ask_user_number2(), ask_user_for_operator())}")
    if ask_user_for_number2() == 00 or ask_user_for_number1() == 00 or ask_user_for_operator() == 00:
        print("Thank you for using the calculator!!!")
        repeat = False
    else:
        answer = calculator(ask_user_for_number1(), ask_user_for_number2(), ask_user_for_operator())
        print(f"The answer is {answer}")