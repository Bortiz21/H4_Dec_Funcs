# Homework 4:  Numeric Processing
# Program By:  Brandon Ortiz
# File Name:   H4_Dec_Funcs.py
# Function:    This Program reads and writes to files

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
def calc():
    print("TBD")


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


menu_choice = int(menu())
operand_1 = int(get_operand())
operand_2 = int(get_operand())

if menu_choice == 1:
    print("Performing Add")
    print("Result:", add(operand_1, operand_2))

elif menu_choice == 2:
    print("Performing Subtract")
    result = (operand_1 - operand_2)
    print("Result: ", result)
else:
    print("error")
