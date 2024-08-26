import turtle

def curve(lenght,n):
    if n==1:
        turtle.forward(lenght)
    else:
        turtle.right(45)
        curve(lenght,n-1)
        turtle.left(180-n*45)
        curve(lenght,n-1)
