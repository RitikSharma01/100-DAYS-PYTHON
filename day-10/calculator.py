
# import art

def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def multi(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


calculation = {'+': add,
               '-': sub,
               '*': multi,
               '/': div
               }


def calculator():
    'YOu can do all calculation'
    num1 = float(input("What's the first number? "))

    for i in calculation:
        print(i)

    operation = input("""What operation you want to execute ? """)

    num2 = float(input("What's the second number? "))
    result_cal = calculation[operation]
    answer = result_cal(num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")
    does_continue = input(
        f"Type 'y' to continue calculating with {answer},or type 'n' to exit: ")
    while does_continue == 'y':
        operation = input("""What operation you want to execute ? """)
        num3 = float(input("What's the next number?: "))
        result_cal = calculation[operation]
        result = result_cal(answer, num3)
        print(f"{answer} {operation} {num3} = {result}")
        answer = result
        does_continue = input(
            f"Type 'y' to continue calculating with {result},or type 'n' to exit: ")
    do_reset = input("do you want to calculate more?(yes/no)")
    if do_reset == 'yes':
        calculator()


calculator()
