#!/usr/bin/env python3

def calculate(arg):
    stack = []
    for operand in arg.split():
        if operand == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(float(operand))
    return stack.pop()

def main():
    while True:
        rst = calculate(input("rpn calc> "))
        print('Result:',rst)

if __name__ == '__main__':
    main()
