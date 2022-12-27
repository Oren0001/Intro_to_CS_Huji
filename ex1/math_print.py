########################################################################
# FILE : hello_turtle.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: Program that Prints to the screen using the math module.
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one.
# WEB PAGES I USED: None.
# NOTES: None.
########################################################################
import math

def golden_ratio():
    """Prints the golden ratio"""
    print((1+math.sqrt(5)) / 2)

def six_squared():
    """Prints 6 to the power of 2"""
    print(math.pow(6, 2))

def hypotenuse():
    """Prints the hypotenuse of a triangle, which his legs are 5 and 12"""
    print(math.sqrt(math.pow(5, 2)+math.pow(12, 2)))

def pi():
    """Prints value of the number pi"""
    print(math.pi)

def e():
    """Prints value of the number e"""
    print(math.e)

def squares_area():
    """Prints the squares area with the sides 1-10"""
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2), math.pow(4, 2),
          math.pow(5, 2), math.pow(6, 2), math.pow(7, 2), math.pow(8, 2),
          math.pow(9, 2), math.pow(10, 2))

if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
