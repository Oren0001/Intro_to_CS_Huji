##########################################################################
# FILE : shapes.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Calculate the shape area of a circle, a rectangle
#              or a triangle.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################
import math


def shape_area():
    """The function returns the shape area of a circle, a rectangle or
    a triangle, following the user's choice"""
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if shape != "1" and shape != "2" and shape != "3":
        return None
    elif shape == "1":
        return circle_area()
    elif shape == "2":
        return rectangle_area()
    elif shape == "3":
        return triangle_area()


def circle_area():
    """Returns a circle area"""
    radius = float(input())
    return math.pi * math.pow(radius, 2)


def rectangle_area():
    """Returns a rectangle area"""
    side1 = float(input())
    side2 = float(input())
    return side1*side2


def triangle_area():
    """Returns an equilateral triangle area"""
    side = float(input())
    return math.pow(side, 2) * math.sqrt(3)/4
