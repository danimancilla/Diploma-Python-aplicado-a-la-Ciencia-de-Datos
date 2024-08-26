import turtle

turtle.left(90)
def fractal(largo,n):
    if n>0:
        turtle.forward(largo)
        turtle.left(30)
        fractal(largo*2/3,n-1)
        turtle.right(60)
        fractal(largo*2/3,n-1)
        turtle.left(30)
        turtle.backward(largo)
