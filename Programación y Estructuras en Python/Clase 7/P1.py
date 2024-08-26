# verificar :: [int] -> bool
# verifica si los elementos de una lista se repiten o no. si no hay repeticiones
# entrega True. si hay repeticiones entrega False
# Ej. verificar([1,2,3,3]) entrega False (porque el 3 se repite)

def verificar(L):
    for elemento in L:
        if L.count(elemento)!=1:
            return False      
    return True

assert verificar([1,2,3,3]) == False
assert verificar([1,2,3,4]) == True
assert not verificar([1,2,3,3])
assert verificar([1,2,3,4])
    
# ok :: [[int]], int, int, int, int -> bool
# verifica si los elementos de una tabla (matriz) se repiten o no. si no hay repeticiones
# entrega True. si hay repeticiones entrega False.
# Ej.  T=[[1,2,3],[3,1,2],[2,3,1]]. ok(T,1,0,1,2) entrega True


def ok(T,c1,f1,c2,f2):
    L = []
    i = f1
    j = c1
    while i <= f2:
        j=c1
        while j <= c2:
            L.append(T[i][j])
            j += 1
        i += 1
    return verificar(L)

T=[[1,2,3],[3,1,2],[2,3,1]]
assert ok(T,1,0,1,2) == True
assert ok(T,0,2,1,2) == True
assert ok(T,0,0,1,1) == False

    
