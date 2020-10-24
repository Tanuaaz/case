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


def main():
    '''
    Main function.
    :return: None
    '''
    #top left figure
    parallelogram(-300, 320, 30, 50, '#9acd32', 0)
    square(-245, 282, 35, '#ff9900', 45)
    triangle(-318, 195, 70, '#dc143c', 0)
    triangle(-245, 170, 30, '#de71e2', 45)
    triangle(-250, 192, 70, '#fefe22', 180)
    triangle(-318, 120, 45, '#6ab8e3', 0)
    triangle(-270, 155, 35, '#8b00ff', 270)

    #top middle figure
    parallelogram(-60, 220, 30, 50, '#9acd32', 45)
    triangle(-123, 187, 30, '#8b00ff', 0)
    triangle(-60, 218, 30, '#ff00ff', 180)
    square(-1, 218, 40, '#ff9900', 0)
    triangle(0, 220, 70, '#dc143c', 90)
    triangle(-70, 145, 70, '#fefe22', 0)
    triangle(3, 182, 50, '#6ab8e3', 45)

    #top right figure
    parallelogram(136, 190, 30, 50, '#9acd32', 90)
    triangle(187, 192, 70, '#dc143c', 90)
    triangle(188, 265, 50, '#6ab8e3', 135)
    triangle(260, 220, 70, '#fefe22', 180)
    triangle(240, 195, 35, '#8b00ff', 225)
    square(262, 223, 40, '#ff9900', 45)
    triangle(270, 265, 35, '#ff00ff', 135)

    #bottom left figure
    triangle(-290, -137, 35, '#8b00ff', 270)
    triangle(-290, -275, 70, '#dc143c', 45)
    triangle(-365, -265, 70, '#fefe22', 0)
    square(-214, -253, 35, '#ff9900', 0)
    triangle(-242, -278, 33, '#de71e2', 135)
    triangle(-311, -280, 50, '#6ab8e3', 315)
    parallelogram(-345, -280, 30, 50, '#9acd32', 225)

    #bottom middle figure
    square(-150, -253, 35, '#ff9900', 0)
    triangle(-113, -270, 34, '#de71e2', 315)
    triangle(-37, -296, 35, '#8b00ff', 135)
    triangle(-9, -220, 70, '#fefe22', 225)
    triangle(-9, -217, 50, '#6ab8e3', 135)
    parallelogram(67, -196, 30, 50, '#9acd32', 0)
    triangle(-5, -318, 70, '#dc143c', 45)

    #bottom right figure
    triangle(145, -325, 30, '#8b00ff', 45)
    square(190, -279, 31, '#ff9900', 0)
    triangle(218, -205, 70, '#dc143c', 225)
    parallelogram(242, -328, 30, 50, '#9acd32', 90)
    triangle(167, -252, 70, '#fefe22', 45)
    triangle(217, -200, 49, '#6ab8e3', 90)
    triangle(216, -149, 32, '#ff00ff', 135)

    turtle.done()


turtle.hideturtle()
if __name__ == '__main__':
    main()