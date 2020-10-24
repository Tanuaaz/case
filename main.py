# Case-study #1
# Developers:   Kostylev M. (33,3%),
#               Turchinovich M. (33,3%),
#               Zubareva T. (33,3%)
import turtle
import math

def parallelogram(x, y, a, b, c, d):
    '''
    Function, drawing parallelogram.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a parallelogram
    :param b: side length of a parallelogram
    :param c: color of a parallelogram
    :param d: turtle turning angle to start drawing new figure
    :return: None
    '''
    turtle.up()
    turtle.speed(20)
    turtle.setposition(x, y)
    turtle.right(d)
    turtle.color(c)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()


def square(x, y, a, b, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.right(c)
    turtle.down()
    turtle.color(b)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.right(c)

def triangle (x, y, a, c, d):
    '''
    Function, drawing triangle.
    :param x: upper corner coordinate x
    :param y: upper corner coordinate y
    :param a: side length of a triangle
    :param c: color of a triangle
    :param d: turtle turning angle to start drawing new figure
    :return: None
    '''
    b = math.sqrt (2 * a**2)
    turtle.up()
    turtle.home()
    turtle.setposition(x, y)
    turtle.left(d)
    turtle.color(c)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(b)
    turtle.end_fill()
    turtle.right(d)
