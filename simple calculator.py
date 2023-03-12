number1 = float(input("enter number 1: "))
number2 = float(input("enter number 2: "))

operation = input("enter operation ('+','-','/','*': )")
while True:
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
       answer = number1 - number2
    elif operation == '/':
        answer = number1 / number2
    elif operation == '*':
        answer = number1 * number2
    else: 
        print("please enter valid operation.")
    print(answer)
    break