"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    inp = raw_input("> ")
    inp_list = inp.split(" ")

    if inp_list[0] == "q":
        print "quit"
        break

    elif inp_list[0] == "+":

        print add(inp_list[1:])

    elif inp_list[0] == "-":
        print subtract(int(inp_list[1]), int(inp_list[2]))

    elif inp_list[0] == "*":
        print multiply(int(inp_list[1]), int(inp_list[2]))

    elif inp_list[0] == "/":
        print divide(int(inp_list[1]), int(inp_list[2]))

    elif inp_list[0] == "square":
        print square(int(inp_list[1]))

    elif inp_list[0] == "cube":
        print cube(int(inp_list[1]))

    elif inp_list[0] == "pow":
        print power(int(inp_list[1]), int(inp_list[2]))

    elif inp_list[0] == "mod":
        print mod(int(inp_list[1]), int(inp_list[2]))

    else:
        print "invalid input. Try again."
