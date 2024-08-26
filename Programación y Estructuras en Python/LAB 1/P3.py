# Integrantes: Dusan Cotoras, Daniela Mancilla, Jenifer Villarroel
# sumatoria :: float int -> float
# calcula los primeros N términos de la suma 1/x^0 + 1/x^1 + 1/x^2 + … + 1/x^N.
# Ej. sumatoria(2,3) entrega 1/1+1/2+1/4+1/8

def sumatoria(x,N):
    suma=1/1
    i=1
    while i<=N:
        suma=suma+1/(x**i)
        i+=1
    return suma
        
#Tests
assert abs(sumatoria(2,3) -(1/1+1/2+1/4+1/8))<0.001
assert abs(sumatoria(2,0) - 1.0) <0.001
assert abs(sumatoria(1,3) -(1/1+1/1+1/1+1/1))<0.001
assert abs(sumatoria(23,1) -(1/1+1/23))<0.001

"""
x=float(input("x? "))
while x!=0:
    n=0
    while n<21:
        suma=sumatoria(x,n)
        print("n = " +str(n) + ", suma = " + str(suma))
        n+=1

    if  abs(sumatoria(x,20)-sumatoria(x,19))<0.001:
        print("converge = sí")
    else:
        print("converge = no")
    x=float(input("x? "))   
print("fin")
"""

x=float(input("x? "))
while x!=0:
    n=0
    while abs(sumatoria(x,n+1)-sumatoria(x,n))>0.001 and n<21:
        suma=sumatoria(x,n)
        print("n = " +str(n) + ", suma = " + str(suma))
        n+=1

    if  abs(sumatoria(x,20)-sumatoria(x,19))<0.001:
        print("converge = sí")
    else:
        print("converge = no")
    x=float(input("x? "))   
print("fin")

