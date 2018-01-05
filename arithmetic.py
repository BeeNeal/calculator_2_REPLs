"""Math functions for calculator."""


def add(lst):
    """Return the sum of the two inputs."""

    return sum(lst)


def subtract(lst):
    """Return the second number subtracted from the first."""

    return reduce(lambda x, y: x - y, lst)


def multiply(lst):
    """Multiply the two inputs together."""

    return reduce(lambda x, y: x * y, lst)


def divide(lst):
    """Divide the first input by the second and return the result."""

    return reduce(lambda x, y: x / y, lst)
#    return float(num1) / num2


def square(lst):
    """Return the square of the input."""

    # Needs only one argument
    return [i ** 2 for i in lst]

    # return num1 * num1


def cube(lst):
    """Return the cube of the input."""

    # Needs only one argument
    # return num1 * num1 * num1

    return [i ** 3 for i in lst]



def power(lst):
    """Raise num1 to the power of num and return the value."""

    # return num1 ** num2
    return reduce(lambda x, y: x ** y, lst)


def mod(lst):
    """Return the remainder of num / num2."""

    return reduce(lambda x, y: x % y, lst)
