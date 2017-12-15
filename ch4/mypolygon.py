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

    angle = 360/n
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
