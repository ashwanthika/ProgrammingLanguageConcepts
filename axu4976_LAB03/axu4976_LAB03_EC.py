# Ashwanthika Umasankar
# UTA ID - 1001854976
#Date of submission: 07/28/2023
# Python version used - Python 3.9.13
# OS -  Windows
import os
def op_check(token):
    # dict that checks if token is an operator and return its type
    operators = {
        "+": "binary_add",
        "-": "binary_subtract",
        "*": "binary_multiply",
        "/": "binary_divide",
        "%": "binary_modulo",
        "unary-": "unary_subtract",
    }
    return operators.get(token, "unknown_operator")

def priority_check(operator):
    #Dictionary to get the priority of operators for RPN conversion
    priority_check = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "unary-": 3}
    return priority_check.get(operator, 0)
def rpn_compute(expression):
    # Function to evaluate RPN expression
    stack = []
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
        "%": lambda x, y: x % y,
        "unary-": lambda x: -x,
    }

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            result = operators[token](num1, num2) if token != "unary-" else operators[token](num2)
            stack.append(result)
    return stack[0]

def infix_eval(expression):
    # Function to convert infix expression to RPN
    op = []
    stack = []

    operators = {"+", "-", "*", "/", "%", "unary-"}
    for token in expression.split():
        if token.isdigit():
            op.append(token)
        elif token in operators:
            while (
                stack
                and op_check(stack[-1])
                and (priority_check(stack[-1]) >= priority_check(token))
            ):
                op.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                op.append(stack.pop())
            stack.pop()  

    while stack:
        op.append(stack.pop())

    return " ".join(op)


def main():
    # Read RPN expressions from input file and print results
    path_os = os.path.join(os.path.dirname(__file__), 'input_RPN_EC.txt')

    with open(path_os, "r") as fl:
        for inp in fl:
            before_conversion = inp.strip()
            rpn = infix_eval(before_conversion)
            output = rpn_compute(rpn)

            print("Input algebraic :", before_conversion)
            print("converted RPN :", rpn)
            print("Final Result:", output)
            print()


if __name__ == "__main__":
    main()

