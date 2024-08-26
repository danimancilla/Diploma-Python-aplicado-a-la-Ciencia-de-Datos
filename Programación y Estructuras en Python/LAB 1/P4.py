#Integrantes: Dusan Cotoras, Daniela Mancilla, Jenifer Villarroel
#Dos jugadores en turnos alternados deben extraer cada vez
#1, 2 o 3 fichas de un montón. Pierde quien extrae la(s) última(s) ficha(s).


import random

N=random.randint(10,20)
print("fichas = " + " O "*N)

while N>0:
    
    jug_1=int(input("jugador 1? "))
    while jug_1<1 or jug_1>3 or jug_1>N:
        print("error")
        jug_1=int(input("jugador 1? "))   
    N=N-jug_1
    if N>0:
        print("fichas = " + " O "*N)
    else:
        print("GANA JUGADOR 2!!!")
        break


    jug_2=int(input("jugador 2? "))
    while jug_2<1 or jug_2>3 or jug_2>N:
        print("error")
        jug_2=int(input("jugador 2? ")) 
    N=N-jug_2
    if N>0:
        print("fichas = " + " O "*N)
    else:
        print("GANA JUGADOR 1!!!")
        break




