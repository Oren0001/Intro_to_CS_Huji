##########################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Calculate mathematical expressions.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################


def calculate_mathematical_expression(num1, num2, operator):
    """
    :param num1: Float or int number.
    :param num2: Another float or int number.
    :param operator: One of the strings: "/", "*", "-", "+".
    :return: Calculation result.
    """
    if operator == "+":
        return num1+num2
    elif operator == "*":
        return num1*num2
    elif operator == "-":
        return num1-num2
    elif operator == "/" and num2 != 0:
        return num1/num2
    else:
        return None


def calculate_from_string(exp):
    """
    :param exp: String that represents expression with the format -
                number 1, space, operator, space, number 2.
    :return: Calculation result.
    """
    num1, operator, num2 = exp.split()
    num1, num2 = float(num1), float(num2)
    return calculate_mathematical_expression(num1, num2, operator)
