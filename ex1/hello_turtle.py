#######################################################################
# FILE : hello_turtle.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A program that draws 3 flowers using the turtle module.
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one.
# WEB PAGES I USED: None.
# NOTES: None.
#######################################################################
import turtle


def draw_petal():
    """This function draws a single petal"""
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    """This function draws a single flower"""
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    """This function draws a single flower,
    and also moves the turtle head to the next position"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """This functions draws 3 flowers"""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()
