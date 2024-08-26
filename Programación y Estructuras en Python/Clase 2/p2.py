import p1
import turtle

"""def casa(n):
    p1.triangulo(n)
    turtle.left(30)
    p1.cuadrado(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    p1.paralelogramo(3*n,n,90)
    turtle.left(180)
    turtle.forward(n)
    turtle.right(90)
    p1.paralelogramo(3*n,n,120)
"""


def casa(n):
    p1.triangulo(n)
    turtle.left(30)
    p1.cuadrado(n)
    turtle.backward(n)
    turtle.left(180)
    p1.paralelogramo(3*n,n,120)
    turtle.right(30)
    turtle.forward(n)
    turtle.left(90)
    p1.paralelogramo(3*n,n,90)


