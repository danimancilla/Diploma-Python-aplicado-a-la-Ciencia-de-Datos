# promedio :: int -> float
# calcula el promedio de las notas entregadas consecutivamentes en un entero
# Ej: promedio(102030) entrega 2.0
# caso base: se acaban las notas
    #se calcula el promedio
# caso recursivo: extraer la nota y guardarla
    #llamar a la función

def promedio(N,suma=0,notas=0):
    if N<100:
        suma=suma+N
        notas=notas+1
        return float(suma/(10*notas))
    else:
        resto=N%100
        N=N//100
        return promedio(N,suma+resto,notas+1)
    
    
assert promedio(102030)==2.0
assert promedio(10)==1.0



# minima :: int -> float
# entrega la nota mínima de las notas entregadas consecutivamentes en un entero
# Ej: minimo(102030) entrega 1.0

def minimo(N,min=70):
    if N<100:
        if N<min:
            return N/10.0
        return min/10.0
    else:
        resto=N%100
        N=N//100
        if resto<min:
            return minimo(N,resto)
        return  minimo(N,min)
    
    
assert minimo(102030)==1.0
assert minimo(402030)==2.0
assert minimo(10)==1.0


# maxima :: int -> float
# entrega la nota máxima de las notas entregadas consecutivamentes en un entero
# Ej: minimo(102030) entrega 3.0

def maxima(N,max=10):
    if N<100:
        if N>max:
            return N/10.0
        return max/10.0
    else:
        resto=N%100
        N=N//100
        if resto>max:
            return maxima(N,resto)
        return  maxima(N,max)
    
    
assert maxima(102030)==3.0
assert maxima(402030)==4.0
assert maxima(10)==1.0
