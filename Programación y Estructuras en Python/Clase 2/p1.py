#cuadrado:: int -> figura
#Dibuja el cuadrado utilizando funcion turtle
#Ej: cuadrado(100) -> Dibuja un cuadrado de lado 100

import turtle
def cuadrado(n):
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)

#triangulo:: int -> figura
#Dibuja el triángulo equilátero utilizando funcion turtle
#Ej: triangulo(100) -> Dibuja un triangulo equilatero de lado 100
    
def triangulo(n):
    turtle.forward(n)
    turtle.left(120)
    turtle.forward(n)
    turtle.left(120)
    turtle.forward(n)

#paralelogramo int int int -> figura
#Dibujar el paralelogramo utilizando funcion turtle
#Ej: paralelogramo(10,5,20) -> Dibuja un paralelotramo de largo 10, ancho 5 y
#y angulo 20 con respecto a la horizontal que forma el lado con la base

def paralelogramo(l1,l2,ang):
    turtle.forward(l1)
    turtle.left(ang)
    turtle.forward(l2)
    turtle.left(180 - ang)
    turtle.forward(l1)
    turtle.left(ang)
    turtle.forward(l2)
