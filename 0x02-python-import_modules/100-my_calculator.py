#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argv = (sys.argv)
    argc = len(argv) - 1

    if argc != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if op == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif op == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif op == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif op == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
