#!/usr/bin/env python3

import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}




def calculate(arg):
    stack = []


    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_func = OPERATORS[operand]
            result = operator_func(arg1, arg2)
            stack.append(result)

    return stack.pop()

def main():
    while True:
        rst = calculate(input("rpn calc> "))
        print('Result:',rst)

if __name__ == '__main__':
    main()
