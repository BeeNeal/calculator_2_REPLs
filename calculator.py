"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    inp = raw_input("> ")
    inp_list = inp.split(" ")

    # make validation function with below code, then add as an elif
    # for item in inp_list[1:]:
    #     if not item.isdigit():
    #         print "invalid input."
    #         continue

    integer_list = [int(i) for i in inp_list[1:]]


    if inp_list[0] == "q":
        print "quit"
        break

    elif inp_list[0] == "+":

        print add(integer_list)

    elif inp_list[0] == "-":
        print subtract(integer_list)

    elif inp_list[0] == "*":
        print multiply(integer_list)

    elif inp_list[0] == "/":
        print divide(integer_list)

    elif inp_list[0] == "square":
        print square(integer_list)

    elif inp_list[0] == "cube":
        print cube(integer_list)

    elif inp_list[0] == "pow":
        print power(integer_list)

    elif inp_list[0] == "mod":
        print mod(integer_list)

    else:
        print "invalid input. Try again."
