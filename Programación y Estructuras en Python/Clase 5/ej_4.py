import math

#cerca: num num num -> bool
#indica si dos cantidades son iguales, con precision epsilon
#ejemplo: cerca(0.1,0.1,0.0001) es verdadero

def cerca(x,y,eps):
    return abs(x - y) < eps

#raiz:: float -> float
#la funcion raiz(x,N) entrega el término N-avo de la aprox de raiz cuadrada de x,
#Ej. raiz(4,20) entrega 2, raiz(16,20) entrega 4

def raiz(x,N):
    r=x/2
    contador=0
    while contador<N:
        contador+=1
        r=1/2*(r+x/r)
    return r

#Tests
margen=0.01
assert cerca(raiz(4,20), 2, margen)
assert cerca(raiz(16,20), 4, margen)
assert cerca(raiz(7,20), math.sqrt(7), margen)
assert cerca(raiz(1,20), 1, margen)


x=float(input("A qué número le quiere calcular la raíz cuadrada? "))
print("N " + "raiz de " + str(x))
print(str(0) + " " + str(raiz(x,0)))

contador=1
while abs(raiz(x,contador)-math.sqrt(x))>1/10**10:
    print(str(contador)+ " "+ str(raiz(x,contador)))
    contador+=1

