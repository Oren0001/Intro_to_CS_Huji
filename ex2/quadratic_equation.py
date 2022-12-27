##########################################################################
# FILE : quadratic_equation.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Solve quadratic equations.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################
import math


def quadratic_equation(a, b, c):
    """The function gets 3 coefficients of a quadratic equation,
    and returns it's solutions"""
    delta = math.pow(b, 2) - 4*a*c
    if delta < 0:
        return None, None
    elif delta == 0:
        return -b / (2*a), None
    else:
        return (-b+math.sqrt(delta)) / (2*a), (-b-math.sqrt(delta)) / (2*a)


def quadratic_equation_user_input():
    """The function asks the user for 3 coefficients, and returns
    the quadratic equation's solution"""
    a, b, c = input("Insert coefficients a, b, and c: ").split()
    if a == "0":
        print("The parameter 'a' may not equal 0")
        return
    x1, x2 = quadratic_equation(float(a), float(b), float(c))
    if (x1 is not None) and (x2 is not None):
        print(f"The equation has 2 solutions: {x1} and {x2}")
    elif (x1 is not None) and (x2 is None):
        print(f"The equation has 1 solution: {x1}")
    else:
        print("The equation has no solutions")
