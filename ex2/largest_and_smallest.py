##########################################################################
# FILE : largest_and_smallest.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Find the largest and the smallest values out of 3 numbers.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################


def largest_and_smallest(num1, num2, num3):
    """This function Gets 3 numbers(int or float), and returns the largest
     value and the smallest value between them"""
    if num1 >= num2:
        max_val, min_val = num1, num2
    else:
        max_val, min_val = num2, num1
    if num3 >= max_val:
        max_val = num3
    elif num3 <= min_val:
        min_val = num3
    return max_val, min_val


def check_largest_and_smallest():
    # My first choice was made to check if the function can handle
    # 3 parameters that are the same.
    # The second choice checks what happens if the second parameter
    # is the largest, and the third is the smallest.
    result = 0
    if largest_and_smallest(17, 1, 6) == (17, 1):
        result += 1
    if largest_and_smallest(1, 17, 6) == (17, 1):
        result += 1
    if largest_and_smallest(1, 1, 2) == (2, 1):
        result += 1
    if largest_and_smallest(-0.66, -0.66, -0.66) == (-0.66, -0.66):
        result += 1
    if largest_and_smallest(5, 9, 3) == (9, 3):
        result += 1
    if result == 5:
        return True
    else:
        return False
