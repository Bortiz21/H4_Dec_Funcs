# Homework 4:  Numeric Processing
# Program By:  Brandon Ortiz
# File Name:   H4_Dec_Funcs.py
# Function:    This Program reads and writes to files
import sys
# Define Functions
# Menu
def menu():
    print(
        '''
Enter an operation :\n
1 Add
2 Subtract
3 Multiple
4 Divide
0 Quit
'''
    )
    user_choice = input()
    return user_choice


# calc
def calc(x):
    try:
        if x == 1:
            print("Performing Add")
            print("Result:", add(operand_1, operand_2))
        elif x == 2:
            print("Performing Subtract")
            result = (operand_1 - operand_2)
            print("Result: ", result)
        elif x == 3:
            print("Performing Multiply")
            result = (operand_1 * operand_2)
            print("Result: ", result)
        elif x == 4:
            print("Performing Division")
            result = (operand_1 / operand_2)
            print("Result: ", result)
        else:
            print("error")
    except:
        print("Invalid input")


# get_operand
def get_operand():
    return input("Enter an operand :")


# add
def add(x, y):
    return x + y


# sub
def sub(x, y):
    return x - y


# mult
def mult(x, y):
    return x * y


# div
def div(x, y):
    return x / y


# input_val
def menu_val(i):
    if i < 0 or i > 4:
        print("Invalid Input, please input a number between 0 - 4.\nTerminating program.")
    else:
        calc(i)


try:
    menu_choice = int(menu())
except:
    print("Invalid Input")
    sys.exit(1)
operand_1 = int(get_operand())
operand_2 = int(get_operand())

test_var_1 = 1
test_var_2 = 999

menu_val(int(menu_choice))
