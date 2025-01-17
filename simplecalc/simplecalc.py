#Simple Calculator

#Init
#Function
operation = input("(1-5)Operation:")
def add(num1, num2):
    result = num1 + num2
    print("The result is: " + str(result))
def subtract(num1, num2):
    result = num1 - num2
    print("The result is: " + str(result))
def divide(num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))
def multiply(num1, num2):
    result = num1 * num2
    print("The result is: " + str(result))
#Main
    print("Welcome Preschoolers to Simple Calculator")
while True:
    print("Enter an operation:")
    print("""1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
    5.Quit""")
    activity = int(input("(1-5)Operation:"))
    if activity == 1 : #True
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        add(int1,int2)
    operation = int(input("(1-5)Operation:"))
    if operation == 2 : #True
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        subtract(int1,int2)
    operation = int(input("(1-5)Operation:"))
    if operation == 3 : #True
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        divide(int1,int2)
    operation = int(input("(1-5)Operation:"))
    if operation == 4 : #True
        int1 = int(input("Enter your first number:"))
        int2 = int(input("Enter your second number:"))
        multiply(int1,int2)
    if activity == 5:
        print("Bye Bye")
