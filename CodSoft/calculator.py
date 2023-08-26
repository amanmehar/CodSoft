#-----------------------------------------------------FINAL-----------------------------------------------------

add = lambda num1, num2 : num1 + num2
subtract = lambda num1, num2 : num1 - num2
multiply = lambda num1, num2 : num1 * num2
divide = lambda num1, num2 : num1 / num2
mod = lambda num1, num2 : num1 % num2

def calculator():

    print('''
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Modulo Division
    ''')

    operation  = input("Select the Operation 1, 2, 3, 4: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(operation == '1'):
        ans : int = add(num1, num2)

    elif(operation == '2'):
        ans : int = subtract(num1, num2)

    elif(operation == '3'):
        ans : int = multiply(num1, num2)

    elif(operation == '4'):
        ans : int = divide(num1, num2)

    elif(operation == '5'):
        ans : int = mod(num1, num2)

    else:
        print('wrong choice')
        return

    print(ans)

if __name__ == "__main__":
    calculator()
    