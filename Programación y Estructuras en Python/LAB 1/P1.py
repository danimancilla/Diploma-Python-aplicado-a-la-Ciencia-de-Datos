# Integrantes: Dusan Cotoras, Daniela Mancilla, Jenifer Villarroel
# perfecto :: int -> bool
# determina si un número es perfecto o no. un número perfecto es igual a la suma de sus divisores
# ej: perfecto(6)-> True (porque 1+2+3=6)

def perfecto(N):
    i=1
    nperfecto=0
    while i<N:
#con el cálculo del resto se pueden determinar los divisores de un número
        resto=N%i
        if resto==0:
#vamos sumando todos los divisores (resto=0)
            nperfecto=nperfecto+i
            i=i+1
        else:
            i=i+1
    return nperfecto==N
    

#Tests
assert perfecto(1)==False
assert perfecto(6)==True
assert perfecto(16)==False



#programa que usa la función anterior para
#determinar y escribir el número perfecto más cercano a 1000.

#partimos con el número entero más bajo n=1 y exploraremos hasta el 10000
n=1
#creamos una diferencia igual al doble del número en cuestión
diferencia_1=2000
#aquí  guardaremos el número que nos interesa
numero=0

while n<10000:
    if perfecto(n) ==True:
        diferencia_2=abs(1000-n)
        if diferencia_2<diferencia_1:
            numero=n
        n=n+1
    else:
        n=n+1
print(numero)



    

