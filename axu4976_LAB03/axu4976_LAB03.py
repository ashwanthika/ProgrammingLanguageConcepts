# Ashwanthika Umasankar
# UTA ID - 1001854976
# Date of submission: 07/28/2023
# Python version used - Python 3.9.13
# OS -  Windows
import os 
def compute(inp):
    #this is a function to evaluate RPN expression. If the char is a digit  we push it to stack, if it is an operator perform the operation on the top of two elements of stack
    stack = []
    op = {"+", "-", "*", "/"}

    for char in inp.split():
        if char.isdigit():
            stack.append(int(char))
        elif char in op:
            var2 = stack.pop()
            var1 = stack.pop()
            output_result = (
                var1 + var2 if char == "+"
                else var1 - var2 if char == "-"
                else var1 * var2 if char == "*"
                else var1 // var2 if char == "/"
                else None  
                )
            stack.append(output_result)

    return stack[0]


def main():
    #Read the expression from input file and evaluate 
    path_os = os.path.join(os.path.dirname(__file__), 'input_RPN.txt')
    with open(path_os, "r") as file:
        for text in file:
            rpn_inp = text.strip()
            output_result = compute(rpn_inp)
            print("The evaluated output_result", output_result)


if __name__ == "__main__":
    main()
