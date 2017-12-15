"""
* Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
  Write a function call that passes bob as an argument to square, and then run the program again.
* Add another parameter, named length, to square. Modify the body so length of the sides is length, 
  and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for length.
* Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. 
  Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
* Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an 
  approximate circle by calling polygon with an appropriate length and number of sides. Test your function with a range of values of r.
  Hint: figure out the circumference of the circle and make sure that length * n = circumference.
* Make a more general version of circle called arc that takes an additional parameter angle, 
  which determines what fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.
"""

import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle
    n: number of sides
    length: length of each segment
    angle: degrees between segments
    """

    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, length, n):
    """Draws polygon.

    t: Turtle
    n: number of sides
    length: length of each segment
    """

    angle = 360 / n
    polyline(t, n=n, length=length, angle=angle)


def circle(t, r):
    """Draws a circle of radius r

    t: Turtle
    r: radius of the circle
    """
    arc(t, r, 360)


def arc(t, r, angle):
    """Draws an arc of circle

    t: Turtle
    r: radius of circle
    angle: arc's angle
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n=n, length=step_length, angle=step_angle)


bob = turtle.Turtle()

#polygon(bob, length=50, n=30)

#circle(bob, r=100)

arc(bob, r=50, angle=45)

turtle.mainloop()
